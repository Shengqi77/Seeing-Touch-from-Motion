# ViTacMotor — Project Page

Project website for **"Seeing Touch from Motion: A Unified Modality-Aware Visuo-Tactile Policy with Tactile Motion Correlation"** (ECCV 2026 submission).

🔗 Live site (after deploying): **https://shengqi77.github.io/ViTacMotor_Web/**

## Structure

```
ViTacMotor/
├── index.html              # single-page project site
├── .nojekyll               # tell GitHub Pages to serve files as-is
├── static/
│   ├── css/style.css
│   ├── images/             # figures exported from the paper
│   ├── videos/             # put task demo .mp4 files here
│   └── pdfs/ViTacMotor.pdf # paper PDF
└── convert_figs.py         # helper used to export figures (not needed for the site)
```

## Deploy to GitHub Pages

The repo is already initialized and committed locally with remote
`https://github.com/Shengqi77/ViTacMotor_Web.git`. Create an **empty** repo named
`ViTacMotor_Web` at github.com/Shengqi77 (no README/.gitignore/license), then push:

```bash
git push -u origin main
```

Then on GitHub: **Settings → Pages → Build and deployment → Source: "Deploy from a branch" → Branch: `main` / `(root)` → Save.**
After ~1 minute the site is live at `https://shengqi77.github.io/ViTacMotor_Web/`.

## To finish later

- **Videos:** drop your task clips into `static/videos/` (e.g. `tube_collection.mp4`). In `index.html`, replace each `<div class="video-placeholder">…</div>` with the commented-out `<video>…</video>` block right below it, and fix the `src`.
- **Authors:** currently "Anonymous Authors" for review. Replace the `publication-authors` block in `index.html` when ready.
- **arXiv link:** update the `arXiv` button `href` in `index.html`.
- **Paper PDF:** `static/pdfs/ViTacMotor.pdf` is the compiled draft (~35 MB). Swap in a lighter / camera-ready version when available.
