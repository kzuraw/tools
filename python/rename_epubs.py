# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "click",
# ]
# ///

"""Rename epub files to 'Author - Title.epub' format."""

import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

import click


def extract_metadata(epub_path: Path) -> tuple[str | None, str | None]:
    """Extract author and title from epub metadata."""
    try:
        with zipfile.ZipFile(epub_path, "r") as zf:
            # Find the OPF file (contains metadata)
            container = zf.read("META-INF/container.xml")
            container_root = ET.fromstring(container)
            ns = {"c": "urn:oasis:names:tc:opendocument:xmlns:container"}
            rootfile = container_root.find(".//c:rootfile", ns)
            if rootfile is None:
                return None, None
            opf_path = rootfile.get("full-path")

            # Parse OPF for metadata
            opf_content = zf.read(opf_path)
            opf_root = ET.fromstring(opf_content)
            dc = {"dc": "http://purl.org/dc/elements/1.1/"}

            title_el = opf_root.find(".//dc:title", dc)
            creator_el = opf_root.find(".//dc:creator", dc)

            title = title_el.text.strip() if title_el is not None and title_el.text else None
            author = creator_el.text.strip() if creator_el is not None and creator_el.text else None

            return author, title
    except Exception:
        return None, None


def sanitize_filename(name: str) -> str:
    """Remove characters that are invalid in filenames."""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        name = name.replace(char, "")
    return name.strip()


@click.command()
@click.argument("folder", type=click.Path(exists=True, file_okay=False, path_type=Path))
@click.option("--dry-run", is_flag=True, help="Preview changes without renaming")
def main(folder: Path, dry_run: bool):
    """Rename epub files in FOLDER to 'Author - Title.epub' format."""
    epubs = list(folder.glob("*.epub"))

    if not epubs:
        click.echo("No epub files found.")
        return

    for epub_path in epubs:
        author, title = extract_metadata(epub_path)

        if not author or not title:
            click.echo(f"Skipping {epub_path.name}: missing metadata")
            continue

        new_name = sanitize_filename(f"{author} - {title}.epub")
        new_path = folder / new_name

        if new_path == epub_path:
            click.echo(f"Already named correctly: {epub_path.name}")
            continue

        if dry_run:
            click.echo(f"Would rename: {epub_path.name} -> {new_name}")
        else:
            epub_path.rename(new_path)
            click.echo(f"Renamed: {epub_path.name} -> {new_name}")


if __name__ == "__main__":
    main()
