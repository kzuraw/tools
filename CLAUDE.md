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
2. Run `pnpm dlx prettier --write "html/**/*.html" "index.html"` and commit changes
3. Add entry to `index.html` tool list
4. Include footer with navigation links:
   - Home link: `../index.html`
   - Source Code link: `https://github.com/kzuraw/tools/blob/main/html/new-tool.html`
   - kzuraw.com link: `https://kzuraw.com`
5. Update README.md html tool list
