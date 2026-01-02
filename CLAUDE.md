# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Collection of web-based HTML tools and Python scripts. All HTML tools run entirely client-side with no server-side processing. Deployed to GitHub Pages at https://kzuraw.github.io/tools/

## Architecture

### HTML Tools Structure

- **`index.html`**: Landing page with links to all tools
- **`html/*.html`**: Individual tool pages, each self-contained
- All tools follow same structure:
  - Vanilla HTML/CSS/JS (no frameworks)
  - Client-side only processing
  - Consistent footer with navigation links
  - Tool emoji favicon: `data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🛠️</text></svg>`
  - Same styling (Apple-inspired, #0071e3 primary color)

### Python Scripts

- **`python/`**: Standalone scripts with inline dependencies (PEP 723)
- Use `uv run` for execution (handles dependencies automatically)

## Development

### Testing HTML Tools

Open HTML files directly in browser. No build process required.

### Python Scripts

```bash
uv run python/rename_invoices.py <directory> [--dry-run]
```

## Deployment

GitHub Pages auto-deploys from `main` branch via `.github/workflows/pages.yml`. Entire repository published at root.

## Adding New Tools

### HTML Tool

1. Create `html/new-tool.html` following existing pattern
2. Add entry to `index.html` tool list
3. Include footer with navigation links
4. Update README.md

### Python Script

1. Add to `python/` directory
2. Use PEP 723 inline dependency spec (see `rename_invoices.py`)
3. Update README.md with usage example
