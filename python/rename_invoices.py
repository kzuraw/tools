# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click",
#     "pypdf",
# ]
# ///

"""Rename invoice PDFs to 'yyyy-mm company_name invoice_number.pdf' format."""

import re
from pathlib import Path

import click
from pypdf import PdfReader


def extract_date_from_pdf(pdf_path: Path) -> tuple[int, int] | None:
    """Extract invoice date (year, month) from PDF content."""
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""

        # Common date patterns in invoices
        # DD.MM.YYYY or DD/MM/YYYY or DD-MM-YYYY
        patterns = [
            r"(\d{1,2})[./\-](\d{1,2})[./\-](20\d{2})",  # DD.MM.YYYY
            r"(20\d{2})[./\-](\d{1,2})[./\-](\d{1,2})",  # YYYY.MM.DD
        ]

        for pattern in patterns:
            matches = re.findall(pattern, text)
            if matches:
                match = matches[0]
                if pattern.startswith(r"(20"):
                    # YYYY.MM.DD format
                    year, month = int(match[0]), int(match[1])
                else:
                    # DD.MM.YYYY format
                    year, month = int(match[2]), int(match[1])
                if 1 <= month <= 12:
                    return year, month

        return None
    except Exception as e:
        click.echo(f"Error reading {pdf_path.name}: {e}", err=True)
        return None


def format_invoice_number(invoice_num: str) -> str:
    """Format invoice number: remove whitespace, convert / to -."""
    # Remove whitespace
    result = re.sub(r"\s+", "", invoice_num)
    # Convert / to -
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
    The date is extracted from the PDF content.
    """
    pdfs = list(folder.glob("*.pdf"))

    if not pdfs:
        click.echo("No PDF files found.")
        return

    renamed_count = 0
    skipped_count = 0

    for pdf_path in pdfs:
        # Check if file already has date prefix (yyyy-mm)
        stem = pdf_path.stem
        if re.match(r"^\d{4}-\d{2}\s", stem):
            click.echo(f"Already has date prefix: {pdf_path.name}")
            continue

        # Extract date from PDF
        date_info = extract_date_from_pdf(pdf_path)
        if not date_info:
            click.echo(f"Skipping {pdf_path.name}: could not extract date")
            skipped_count += 1
            continue

        year, month = date_info

        # Parse filename: first word is company, rest is invoice number
        parts = stem.split(maxsplit=1)
        if len(parts) < 2:
            click.echo(f"Skipping {pdf_path.name}: unexpected filename format")
            skipped_count += 1
            continue

        company_name = parts[0]
        invoice_number = format_invoice_number(parts[1])

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
