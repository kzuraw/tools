# Tools

A collection of web-based and python utility tools. These tools run entirely in the browser with no server-side processing, ensuring privacy and fast performance.

## Available Tools

- **[Certificate to Single Line](https://kzuraw.github.io/tools/html/cert-converter.html)** - convert certificates to single line format
- **[Git Commit Formatter](https://kzuraw.github.io/tools/html/git-commit-formatter.html)** - format commit messages with proper structure and line wrapping
- **[GitHub Alert Copier](https://kzuraw.github.io/tools/html/github-alert-copier.html)** - copy GitHub alerts as HTML
- **[Invoice Path Generator](https://kzuraw.github.io/tools/html/invoice-path-generator.html)** - generate standardized invoice file paths
- **[Link to Markdown Table](https://kzuraw.github.io/tools/html/link-to-markdown-table.html)** - convert links to markdown table format
- **[Markdown to Rich Text](https://kzuraw.github.io/tools/html/markdown-to-rich-text.html)** - convert markdown to rich text

## Python Scripts

### rename_invoices.py

Rename PDF invoice files from "YYYY-MM-DD - name - invoice_no.pdf" to "YYYY-MM-DD_name_invoice_no.pdf" format

```bash
uv run https://kzuraw.github.io/tools/python/rename_invoices.py <directory> [--dry-run]
```

## Usage

Visit [https://kzuraw.github.io/tools/](https://kzuraw.github.io/tools/) to access all tools.

All tools are client-side only - your data never leaves your browser.

### Development

All tools run entirely client-side, so you can test changes by simply opening the HTML files in your browser. No build process or server setup is required.

## Deployment

This project is automatically deployed to GitHub Pages. Any changes pushed to the main branch will be reflected at [https://kzuraw.github.io/tools/](https://kzuraw.github.io/tools/).

## License

MIT License - See [LICENSE](LICENSE) file for details.
