# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click",
# ]
# ///

"""Rename invoice PDFs to 'yyyy-mm company_name invoice_number.pdf' format."""

import re
from datetime import datetime
from pathlib import Path

import click


def get_file_date(file_path: Path) -> tuple[int, int]:
    """Get file creation date (year, month) from file metadata."""
    stat = file_path.stat()
    # Try birth time (creation time), fall back to mtime
    timestamp = getattr(stat, "st_birthtime", None) or stat.st_mtime
    dt = datetime.fromtimestamp(timestamp)
    return dt.year, dt.month


def format_invoice_number(invoice_num: str) -> str:
    """Format invoice number: remove whitespace, convert / to -."""
    result = re.sub(r"\s+", "", invoice_num)
    result = result.replace("/", "-")
    return result


def sanitize_filename(name: str) -> str:
    """Remove characters that are invalid in filenames."""
    invalid_chars = '<>:"|?*'
    for char in invalid_chars:
        name = name.replace(char, "")
    return name.strip()


@click.command()
@click.argument("folder", type=click.Path(exists=True, file_okay=False, path_type=Path))
@click.option("--dry-run", is_flag=True, help="Preview changes without renaming")
def main(folder: Path, dry_run: bool):
    """Rename invoice PDFs in FOLDER to 'yyyy-mm company_name invoice_number.pdf' format.

    Expected input format: 'company_name invoice_number.pdf'
    Output format: 'yyyy-mm company_name invoice_number.pdf'

    The invoice number will have whitespace removed and / converted to -.
    The date is taken from the file creation date.
    """
    pdfs = list(folder.glob("*.pdf"))

    if not pdfs:
        click.echo("No PDF files found.")
        return

    renamed_count = 0
    skipped_count = 0

    for pdf_path in pdfs:
        stem = pdf_path.stem

        # Check if file already has date prefix (yyyy-mm)
        if re.match(r"^\d{4}-\d{2}\s", stem):
            click.echo(f"Already has date prefix: {pdf_path.name}")
            continue

        # Parse filename: first word is company, rest is invoice number
        parts = stem.split(maxsplit=1)
        if len(parts) < 2:
            click.echo(f"Skipping {pdf_path.name}: unexpected filename format")
            skipped_count += 1
            continue

        company_name = parts[0]
        invoice_number = format_invoice_number(parts[1])

        # Get date from file creation time
        year, month = get_file_date(pdf_path)

        # Build new filename
        new_stem = f"{year}-{month:02d} {company_name} {invoice_number}"
        new_name = sanitize_filename(f"{new_stem}.pdf")
        new_path = folder / new_name

        if new_path.exists() and new_path != pdf_path:
            click.echo(f"Skipping {pdf_path.name}: target file already exists")
            skipped_count += 1
            continue

        if dry_run:
            click.echo(f"Would rename: {pdf_path.name} → {new_name}")
        else:
            pdf_path.rename(new_path)
            click.echo(f"Renamed: {pdf_path.name} → {new_name}")
        renamed_count += 1

    if renamed_count == 0 and skipped_count == 0:
        click.echo("\nNo files needed renaming.")
    elif dry_run:
        click.echo(
            f"\nDry run complete. {renamed_count} file(s) would be renamed, {skipped_count} skipped."
        )
    else:
        click.echo(f"\nRenamed {renamed_count} file(s), {skipped_count} skipped.")


if __name__ == "__main__":
    main()
