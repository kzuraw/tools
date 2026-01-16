# Tools

A collection of web-based and python utility tools.

## Available Tools

- **[Certificate to Single Line](https://kzuraw.github.io/tools/html/cert-converter.html)** - convert certificates to single line format
- **[Git Commit Formatter](https://kzuraw.github.io/tools/html/git-commit-formatter.html)** - format commit messages with proper structure and line wrapping
- **[GitHub Alert Copier](https://kzuraw.github.io/tools/html/github-alert-copier.html)** - copy GitHub alerts as HTML
- **[Invoice Path Generator](https://kzuraw.github.io/tools/html/invoice-path-generator.html)** - generate standardized invoice file paths
- **[Link to Markdown Table](https://kzuraw.github.io/tools/html/link-to-markdown-table.html)** - convert links to markdown table format
- **[Markdown to Rich Text](https://kzuraw.github.io/tools/html/markdown-to-rich-text.html)** - convert markdown to rich text
- **[SVG to React](https://kzuraw.github.io/tools/html/svg-to-react.html)** - convert SVG to React components with camelCased props

## Python Scripts

### rename_invoices.py

Rename PDF invoice files from "YYYY-MM-DD - name - invoice_no.pdf" to "YYYY-MM-DD_name_invoice_no.pdf" format

```bash
uv run https://kzuraw.github.io/tools/python/rename_invoices.py <directory> [--dry-run]
```

### rename_epubs.py

Rename epub files to "Author - Title.epub" format using metadata from the epub file

```bash
uv run https://kzuraw.github.io/tools/python/rename_epubs.py <directory> [--dry-run]
```

## Deployment

This project is automatically deployed to GitHub Pages. Any changes pushed to the main branch will be reflected at [https://kzuraw.github.io/tools/](https://kzuraw.github.io/tools/).

## License

MIT License - See [LICENSE](LICENSE) file for details.
