# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## HTML

- **`index.html`**: Landing page with links to all tools
- **`html/*.html`**: Individual tool pages, each self-contained
- All tools follow same structure:
  - Vanilla HTML/CSS/JS (no frameworks)
  - Client-side only processing
  - Consistent footer with navigation links (Home, Source Code pointing to specific file on GitHub, kzuraw.com)
  - Tool emoji favicon: `🛠️`
  - Same styling (Apple-inspired, #0071e3 primary color)

### Adding new html tool

1. Create `html/new-tool.html` following existing pattern
2. Add entry to `index.html` tool list
3. Include footer with navigation links:
   - Home link: `../index.html`
   - Source Code link: `https://github.com/kzuraw/tools/blob/main/html/new-tool.html`
   - kzuraw.com link: `https://kzuraw.com`
4. Update README.md html tool list

## Python

- **`python/`**: Standalone scripts with inline dependencies (PEP 723)
- Use `uv run` for execution (handles dependencies automatically)

### Adding new python script

1. Add to `python/` directory
2. Use PEP 723 inline dependency spec
3. Update README.md with usage example
