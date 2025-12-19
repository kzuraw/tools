#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "click",
# ]
# ///

import click
import os
import re
from pathlib import Path


def convert_filename(filename: str) -> str | None:
    """
    Convert filename from 'YYYY-MM-DD - <name> - <invoice_no>.pdf' 
    to 'YYYY-MM-DD_<name>_<invoice_no>.pdf'
    
    Returns the new filename if pattern matches, None otherwise.
    """
    # Check if it's a PDF file
    if not filename.lower().endswith('.pdf'):
        return None
    
    # Remove the .pdf extension for easier parsing
    name_without_ext = filename[:-4]
    
    # Pattern to match the date at the beginning
    date_pattern = r'^(\d{4}-\d{2}-\d{2})\s*-\s*(.+)$'
    match = re.match(date_pattern, name_without_ext)
    
    if not match:
        return None
    
    date, remainder = match.groups()
    
    # Find the last occurrence of ' - ' to split name from invoice_no
    # This handles cases where the name itself contains ' - '
    last_separator_idx = remainder.rfind(' - ')
    
    if last_separator_idx == -1:
        # No second separator found, doesn't match the pattern
        return None
    
    name = remainder[:last_separator_idx].strip()
    invoice_no = remainder[last_separator_idx + 3:].strip()  # +3 to skip ' - '
    
    # Create new filename with underscores
    new_filename = f"{date}_{name}_{invoice_no}.pdf"
    
    return new_filename


@click.command()
@click.argument('directory', type=click.Path(exists=True, file_okay=False, dir_okay=True))
@click.option('--dry-run', is_flag=True, help='Show what would be renamed without making changes')
def main(directory: str, dry_run: bool):
    """
    Convert invoice filenames from 'YYYY-MM-DD - <name> - <invoice_no>.pdf' 
    to 'YYYY-MM-DD_<name>_<invoice_no>.pdf'
    
    DIRECTORY: Path to the directory containing PDF files to rename
    """
    dir_path = Path(directory)
    
    # Find all PDF files in the directory
    pdf_files = list(dir_path.glob('*.pdf'))
    
    if not pdf_files:
        click.echo(f"No PDF files found in {directory}")
        return
    
    renamed_count = 0
    skipped_count = 0
    
    for pdf_file in pdf_files:
        old_filename = pdf_file.name
        new_filename = convert_filename(old_filename)
        
        if new_filename is None:
            click.echo(f"⏭️  Skipping: {old_filename} (doesn't match pattern)")
            skipped_count += 1
            continue
        
        if old_filename == new_filename:
            click.echo(f"⏭️  Skipping: {old_filename} (already in correct format)")
            skipped_count += 1
            continue
        
        new_path = pdf_file.parent / new_filename
        
        if new_path.exists():
            click.echo(f"⚠️  Warning: {old_filename} -> {new_filename} (destination already exists)")
            skipped_count += 1
            continue
        
        if dry_run:
            click.echo(f"🔍 Would rename: {old_filename} -> {new_filename}")
            renamed_count += 1
        else:
            try:
                pdf_file.rename(new_path)
                click.echo(f"✅ Renamed: {old_filename} -> {new_filename}")
                renamed_count += 1
            except (OSError, PermissionError) as e:
                click.echo(f"❌ Error renaming {old_filename}: {e}")
                skipped_count += 1
    
    # Summary
    click.echo("\n" + "="*50)
    if dry_run:
        click.echo(f"DRY RUN: {renamed_count} files would be renamed, {skipped_count} skipped")
    else:
        click.echo(f"Complete: {renamed_count} files renamed, {skipped_count} skipped")


if __name__ == '__main__':
    main()
