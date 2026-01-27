# Tools

A collection of web-based and python utility tools.

## Available Tools

- **[Certificate to Single Line](https://tools.kzuraw.com/html/cert-converter.html)** - convert certificates to single line format
- **[Git Commit Formatter](https://tools.kzuraw.com/html/git-commit-formatter.html)** - format commit messages with proper structure and line wrapping
- **[GitHub Alert Copier](https://tools.kzuraw.com/html/github-alert-copier.html)** - copy GitHub alerts as HTML
- **[Invoice Path Generator](https://tools.kzuraw.com/html/invoice-path-generator.html)** - generate standardized invoice file paths
- **[Link to Markdown Table](https://tools.kzuraw.com/html/link-to-markdown-table.html)** - convert links to markdown table format
- **[Markdown to Rich Text](https://tools.kzuraw.com/html/markdown-to-rich-text.html)** - convert markdown to rich text
- **[SVG to React](https://tools.kzuraw.com/html/svg-to-react.html)** - convert SVG to React components with camelCased props

## Python Scripts

### rename_epubs.py

Rename epub files to `Author - Title.epub` format using metadata from the epub file

```bash
uv run https://tools.kzuraw.com/python/rename_epubs.py <directory> [--dry-run]
```

### rename_invoices.py

Rename invoice PDFs from `company_name invoice_number.pdf` to `yyyy-mm company_name invoice_number.pdf` format. Extracts the date from PDF content and formats the invoice number (removes whitespace, converts `/` to `-`).

```bash
uv run https://tools.kzuraw.com/python/rename_invoices.py <directory> [--dry-run]
```

## Deployment

This project is automatically deployed to Cloudflare Pages. Any changes pushed to the main branch will be reflected at [https://tools.kzuraw.com/](https://tools.kzuraw.com/).

## License

MIT License - See [LICENSE](LICENSE) file for details.
