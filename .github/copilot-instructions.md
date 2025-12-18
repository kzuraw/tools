# Copilot Instructions for kzuraw/tools

## Repository Summary

This is a collection of web-based utility tools for developers and content creators. All tools run entirely client-side in the browser with no server-side processing, ensuring privacy and fast performance. The repository is deployed to GitHub Pages at https://kzuraw.github.io/tools/.

**Key Facts:**
- **Type:** Static website with client-side JavaScript tools
- **Size:** Small repository (~300KB, 13 files)
- **Languages:** HTML, CSS, JavaScript (vanilla JS, no framework)
- **Deployment:** Automatic via GitHub Pages on push to main branch
- **Runtime:** Browser-only (no build process, no server, no Node.js required)

## Project Structure

```
/
├── .github/
│   └── workflows/
│       ├── pages.yml              # GitHub Pages deployment (automatic)
│       ├── claude.yml              # Claude Code action workflow
│       └── claude-code-review.yml  # Automated code reviews
├── html/                           # Individual tool HTML files
│   ├── cert-converter.html         # Certificate format converter
│   ├── git-commit-formatter.html   # Git commit message formatter
│   ├── github-alert-copier.html    # GitHub alert markdown copier
│   ├── link-to-markdown-table.html # Link to markdown table converter
│   ├── markdown-to-rich-text.html  # Markdown to rich text converter (uses marked.js CDN)
│   └── sql-formatter.html          # SQL query formatter
├── index.html                      # Main landing page with tool list
├── README.md                       # Project documentation
├── LICENSE                         # MIT License
└── .gitignore                      # Python-focused gitignore (legacy)
```

## Build & Validation Process

### IMPORTANT: No Build Process Required

This project has **NO build, compile, or bundling steps**. All tools are self-contained HTML files with inline CSS and JavaScript.

**To test changes:**
1. Simply open the HTML file directly in a browser (e.g., `file:///path/to/index.html`)
2. OR use a local HTTP server: `python3 -m http.server 8000` and visit `http://localhost:8000`
3. Test all interactive functionality manually (buttons, text areas, copy operations)

**No commands to run:**
- No `npm install` or `npm run build`
- No `yarn` or package managers
- No `make` or build scripts
- No test suite exists (manual testing only)
- No linters configured (no ESLint, Prettier, etc.)

### Validation Checklist

Before submitting changes, manually verify:

1. **HTML Validity:** Ensure proper `<!DOCTYPE html>` declaration and closing tags
2. **Links Work:** Check all navigation links (especially to/from index.html)
3. **Tool Functionality:** Test the specific tool's core functionality in a browser
4. **Visual Appearance:** Verify styling is consistent with existing tools
5. **Mobile Responsive:** Test on different viewport sizes if UI changes were made
6. **Browser Console:** Check for JavaScript errors in browser dev tools
7. **Cross-browser:** Test in Chrome/Edge at minimum (Safari/Firefox if possible)

## CI/CD & GitHub Workflows

### 1. GitHub Pages Deployment (pages.yml)
- **Trigger:** Automatically on push to `main` branch OR manual workflow_dispatch
- **What it does:** Deploys the entire repository to GitHub Pages
- **Result:** Site available at https://kzuraw.github.io/tools/
- **Duration:** ~30-60 seconds
- **No failures expected** unless GitHub Pages is down

### 2. Claude Code Action (claude.yml)
- **Trigger:** When `@claude` is mentioned in issues, PR comments, or reviews
- **What it does:** Invokes Claude Code agent to help with tasks
- **Note:** Requires `CLAUDE_CODE_OAUTH_TOKEN` secret

### 3. Claude Code Review (claude-code-review.yml)
- **Trigger:** On PR open or synchronize
- **What it does:** Automated code review via Claude
- **Note:** Requires `CLAUDE_CODE_OAUTH_TOKEN` secret

**IMPORTANT:** Since there's no build or test step, the only CI job that can fail is the Pages deployment, which is extremely rare.

## Architecture & Code Patterns

### Tool File Structure

Each tool in `html/` follows this pattern:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tool Name</title>
    <link rel="icon" href="data:image/svg+xml,...">  <!-- 🛠️ emoji favicon -->
    <style>
        /* Inline CSS - consistent Apple-inspired design system */
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", ...; }
        /* ... */
    </style>
</head>
<body>
    <div class="container">
        <h1>Tool Name</h1>
        <!-- Tool-specific UI -->
    </div>
    <script>
        // Vanilla JavaScript - no frameworks
        // Usually includes clipboard operations, text processing, etc.
    </script>
    <footer>
        <a href="../index.html">Home</a> |
        <a href="https://github.com/kzuraw/tools">Source Code</a> |
        <a href="https://kzuraw.com">kzuraw.com</a>
    </footer>
</body>
</html>
```

### Key Design Principles

1. **Self-contained:** Each tool is a single HTML file with inline CSS and JS
2. **No external dependencies:** Except `markdown-to-rich-text.html` uses marked.js from CDN: `https://cdnjs.cloudflare.com/ajax/libs/marked/9.1.6/marked.min.js`
3. **Consistent styling:** Apple-inspired design (San Francisco-style fonts, rounded corners, subtle shadows)
4. **Privacy-first:** All processing happens client-side; no data sent to servers
5. **Responsive:** Mobile-friendly layouts
6. **Footer navigation:** Every tool page links back to home and GitHub

### Common Patterns

- **Colors:** Primary blue `#007bff` or `#0071e3`, backgrounds `#f5f5f7`, text `#1d1d1f`
- **Typography:** System fonts stack: `-apple-system, BlinkMacSystemFont, "Segoe UI", ...`
- **Monospace:** `"SF Mono", Monaco, monospace` for code/technical content
- **Button animations:** Subtle hover effects, `:active` scale transforms
- **Clipboard API:** Most tools use `navigator.clipboard.writeText()` for copying
- **No jQuery:** Pure vanilla JavaScript throughout

## Adding a New Tool

**Required steps** (as documented in README.md):

1. Create a new HTML file in `html/` directory (copy an existing tool as template)
2. Add the tool to `index.html` in the `<ul class="tool-list">` with format:
   ```html
   <li><a href="html/tool-name.html">Tool Display Name</a> <span class="description">brief description</span></li>
   ```
3. Update README.md "Available Tools" section with the new tool and link
4. Test locally by opening `html/tool-name.html` in a browser
5. Verify footer links work (especially `../index.html` back to home)
6. Commit and push to trigger automatic GitHub Pages deployment

**Tool naming conventions:**
- File names: lowercase with hyphens (e.g., `git-commit-formatter.html`)
- Display names: Title Case with spaces (e.g., "Git Commit Formatter")

## Common Pitfalls & Important Notes

1. **Relative paths:** Tools in `html/` must use `../index.html` to link back to home
2. **No package.json:** Don't try to add npm dependencies; keep tools self-contained
3. **Inline everything:** Don't create separate CSS/JS files; keep tools as single files
4. **CDN dependencies:** Minimize external dependencies; only add if absolutely necessary
5. **Testing:** Always manually test in a browser; there's no automated test suite
6. **Mobile testing:** Use browser dev tools responsive mode to verify mobile layouts
7. **Git ignore:** The .gitignore is Python-focused (legacy) but doesn't affect this HTML project

## Key Files

- **index.html:** Main landing page - update this when adding/removing tools
- **README.md:** Documentation - keep the "Available Tools" section in sync with index.html
- **.github/workflows/pages.yml:** Deployment configuration - rarely needs changes
- **html/*.html:** Individual tool files - self-contained and independently functional

## Validation Philosophy

Since there's no automated testing:
1. **Test in browser immediately** after making changes
2. **Check browser console** for JavaScript errors
3. **Verify all interactive elements work** (buttons, inputs, copy functions)
4. **Test edge cases** for the tool's functionality (empty inputs, large inputs, etc.)
5. **Visual inspection** to ensure styling matches other tools
6. **Links verification** - click all navigation links to ensure they work

## Trust These Instructions

These instructions are comprehensive and validated. Only perform additional searches if:
- You need to understand specific implementation details of a particular tool
- Information here conflicts with what you observe in the code
- You're implementing a feature that requires understanding complex JavaScript logic in an existing tool

For routine tasks (adding tools, fixing bugs, updating styles), this document contains everything you need to work efficiently without exploration.
