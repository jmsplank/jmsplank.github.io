# James Plank (Personal Website)

<p align="center">
   <img src="content/logo.png" width="40%"/>
   <br>
   <a href="https://jamesplank.co.uk">jamesplank.co.uk</a>
</p>

<p align="center">
   <img src="https://img.shields.io/badge/Hugo_version-0.167.0-pink" alt="Static Badge">
   <img src="https://img.shields.io/github/last-commit/jmsplank/jmsplank.github.io/main" alt="GitHub last commit (branch)">
   <img src="https://img.shields.io/github/deployments/jmsplank/jmsplank.github.io/github-pages?logo=github&color=orange" alt="GitHub deployments">
   <img src="https://img.shields.io/website?up_message=online&up_color=blue&down_message=offline&down_color=red&url=https%3A%2F%2Fjamesplank.co.uk%2F" alt="Website">
   <img src="https://img.shields.io/github/license/jmsplank/jmsplank.github.io" alt="GitHub">
</p>

This is the repository for my personal website [jamesplank.co.uk](https://jamesplank.co.uk), created using HUGO and deployed using GitHub pages.

## Install

1. Clone the repository using

   ```bash
   git clone git@github.com:jmsplank/jmsplank.github.io.git
   ```

1. Install Hugo (extended edition, 0.167.0 or newer)

   ```bash
   brew install hugo
   ```

   In CI Hugo is installed by `peaceiris/actions-hugo`, pinned in `.github/workflows/gh-pages-hugo.yml`.

1. Install the other requirements
   ```bash
   cd jmsplank.github.io
   npm ci
   ```
   This installs Tailwind CSS and its CLI, which Hugo runs to build the css.

## About

- The website is made with Hugo static site builder
- Tailwind CSS is used for styling and Alpine.js for small bits of interactivity
- Katex is used to display math
- The theme is entirely custom built

## Structure

### Build scripts

Some useful scripts are in `package.json`, these are:

`npm run dev`: Run the development server, live reload, include draft pages

`npm run dev:nodraft`: As above but drafts are disabled

`npm run build`: Build/compile the Hugo into static html, writes to `public/`

`npm run build:serve`: Start a python http.server running on port 8000 that serves the `public/` dir

### Tailwind CSS

The stylesheet is `assets/css/main.css`. It imports Tailwind, defines the theme colours and fonts in an `@theme` block, and adds some base styles for Markdown content.

Hugo builds it with `css.TailwindCSS`, which runs the Tailwind CLI. To know which classes are used, Hugo writes `hugo_stats.json` (gitignored) during the build and Tailwind scans it via `@source`. Classes must therefore appear in full in templates or content, not be assembled from strings.

The `<link>` is generated in `layouts/_partials/head/tailwind.html`: minified and fingerprinted in production, plain in development. Hugo's `security.exec.allow` in `config/_default/hugo.toml` must include `tailwindcss` for this to run.

### Alpine.js

Alpine is loaded from jsDelivr in `layouts/_partials/head.html`, pinned to a version with an SRI hash. Update both together.