# Seeing Touch from Motion — Project Page

Project website for **"Seeing Touch from Motion: A Unified Modality-Aware Visuo-Tactile Policy with Tactile Motion Correlation"** (ECCV 2026).

🔗 Live site: **https://shengqi77.github.io/ViTacMotor-Web/**
💻 Code (separate repo): https://github.com/Shengqi77/ViTacMotor

## Structure

```
.
├── index.html              # single-page project site
├── .nojekyll               # tell GitHub Pages to serve files as-is
├── static/
│   ├── css/style.css
│   ├── images/             # figures exported from the paper
│   ├── videos/             # task demo .mp4 files (task1_baseline.mp4, task1_ours.mp4, ...)
│   └── pdfs/ViTacMotor.pdf # paper PDF
└── convert_figs.py         # helper used to export figures (not needed for the site)
```

## Deploy / update

This site lives in the GitHub repo **Shengqi77/ViTacMotor-Web** with remote already set.
To publish changes:

```bash
git add -A
git commit -m "Update site"
git push origin main
```

GitHub Pages (Settings → Pages → Deploy from a branch → `main` / `(root)`) rebuilds in ~1 min.
Live at `https://shengqi77.github.io/ViTacMotor-Web/`.

## To finish later

- **Videos:** add more task clips to `static/videos/` named `taskN_baseline.mp4` / `taskN_ours.mp4`.
  In `index.html`, replace each Task 2–4 `<div class="video-placeholder">…</div>` with a
  `<video class="compare-video" controls autoplay muted loop playsinline><source src="..."></video>`
  block (copy the Task 1 markup), and set the real task titles.
- **Authors:** currently "Anonymous Authors". Replace the `publication-authors` block in `index.html`.
- **arXiv link:** update the `arXiv` button `href` in `index.html`.
- **Paper PDF:** `static/pdfs/ViTacMotor.pdf` is the compiled draft (~35 MB). Swap in a lighter / camera-ready version.
