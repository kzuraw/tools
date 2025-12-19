# tools

A collection of utility tools for developers and content creators.

## Web-Based Tools

These tools run entirely in the browser with no server-side processing, ensuring privacy and fast performance.

- **[Certificate Converter](https://kzuraw.github.io/tools/html/cert-converter.html)** - convert certificates between different formats
- **[Git Commit Formatter](https://kzuraw.github.io/tools/html/git-commit-formatter.html)** - format commit messages with proper structure and line wrapping
- **[GitHub Alert Copier](https://kzuraw.github.io/tools/html/github-alert-copier.html)** - copy GitHub alerts as HTML
- **[Link to Markdown Table](https://kzuraw.github.io/tools/html/link-to-markdown-table.html)** - convert links to markdown table format
- **[Markdown to Rich Text](https://kzuraw.github.io/tools/html/markdown-to-rich-text.html)** - convert markdown to rich text
- **[SQL Formatter](https://kzuraw.github.io/tools/html/sql-formatter.html)** - format SQL queries

## Python CLI Tools

Python command-line tools using [PEP 723](https://peps.python.org/pep-0723/) inline script metadata.

### Invoice Filename Renamer (`rename_invoices.py`)

Converts invoice filenames from `YYYY-MM-DD - <name> - <invoice_no>.pdf` to `YYYY-MM-DD_<name>_<invoice_no>.pdf`.

**Features:**
- Dry-run mode to preview changes
- Handles hyphens in company names and invoice numbers
- Clear feedback for each operation

**Usage:**
```bash
# Preview changes without renaming
python3 rename_invoices.py --dry-run /path/to/invoices

# Actually rename files
python3 rename_invoices.py /path/to/invoices

# Can also use uvx if available
uvx rename_invoices.py --dry-run /path/to/invoices
```

## Web Tools Usage

Visit [https://kzuraw.github.io/tools/](https://kzuraw.github.io/tools/) to access all web-based tools.

All web tools are client-side only - your data never leaves your browser.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

### Adding a New Web Tool

1. Create a new HTML file in the `html/` directory
2. Add your tool to `index.html` with a link and description
3. Update this README with the new tool in the Web-Based Tools section
4. Test your tool locally by opening the HTML file in a browser

### Adding a New Python CLI Tool

1. Create a Python script with PEP 723 inline metadata at the top
2. Add the tool to this README in the Python CLI Tools section
3. Make the script executable: `chmod +x script_name.py`
4. Test your tool with `python3 script_name.py` or `uvx script_name.py`

### Development

**Web Tools:** All web tools run entirely client-side, so you can test changes by simply opening the HTML files in your browser. No build process or server setup is required.

**Python Tools:** Python CLI tools use PEP 723 inline script metadata. They can be run with `python3` (with dependencies installed) or with `uvx` which handles dependencies automatically.

## Deployment

This project is automatically deployed to GitHub Pages. Any changes pushed to the main branch will be reflected at [https://kzuraw.github.io/tools/](https://kzuraw.github.io/tools/).

## License

MIT License - See [LICENSE](LICENSE) file for details.
