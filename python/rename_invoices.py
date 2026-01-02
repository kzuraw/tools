# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click",
# ]
# ///

import click
import re
from pathlib import Path


def normalize(text: str) -> str:
    """Convert text to lowercase and replace whitespace with hyphens."""
    return re.sub(r'\s+', '-', text.strip().lower())


@click.command()
@click.argument('directory', type=click.Path(exists=True, file_okay=False, path_type=Path))
@click.option('--dry-run', is_flag=True, help='Show what would be renamed without actually renaming')
def rename_invoices(directory: Path, dry_run: bool):
    """Rename PDF files from 'YYYY-MM-DD - <name> - <invoice_no>.pdf' to 'YYYY-MM-DD_<name>_<invoice_no>.pdf'

    Name and invoice_no are converted to lowercase with whitespace replaced by hyphens.
    """

    pattern = re.compile(r'^(\d{4}-\d{2}-\d{2}) - (.+?) - (.+?)\.pdf$')

    pdf_files = list(directory.glob('*.pdf'))
    renamed_count = 0

    for pdf_file in pdf_files:
        match = pattern.match(pdf_file.name)
        if match:
            date, name, invoice_no = match.groups()
            name = normalize(name)
            invoice_no = normalize(invoice_no)
            new_name = f"{date}_{name}_{invoice_no}.pdf"
            new_path = pdf_file.parent / new_name
            
            if dry_run:
                click.echo(f"Would rename: {pdf_file.name} → {new_name}")
            else:
                pdf_file.rename(new_path)
                click.echo(f"Renamed: {pdf_file.name} → {new_name}")
            
            renamed_count += 1
    
    if renamed_count == 0:
        click.echo("No matching files found.")
    elif dry_run:
        click.echo(f"\nDry run complete. {renamed_count} file(s) would be renamed.")
    else:
        click.echo(f"\nRenamed {renamed_count} file(s).")


if __name__ == '__main__':
    rename_invoices()
    
