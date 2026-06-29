import fitz  # PyMuPDF
from PIL import Image
import io, os

BASE = r"D:/Doctor/paperwriting_exp/2026_boundary_tactile/Paper_2026_ECCV_only_tactile/camera_ready_version/camera_ready_final/Figure_arxiv_compress"
DST = r"C:/Users/XSQ/ViTacMotor/static/images"

# map: source pdf (relative to BASE) -> output png name (camera_ready_final main-text figures)
figs = {
    "Figure1_arxiv.pdf": "teaser.png",
    "Figure2_arxiv_3.pdf": "method.png",
    "Figure3_arxiv_2.pdf": "tmc_analysis.png",
    "Figure4_arxiv_0629.pdf": "setup.png",
    "Figure5_arxiv_0629_strong.pdf": "qualitative.png",
    "Figure6_arxiv.pdf": "robustness.png",
}

ZOOM = 3.0       # ~216 DPI
MAXW = 2000      # cap width for web

for src, out in figs.items():
    path = os.path.join(BASE, src)
    if not os.path.exists(path):
        print("MISSING", path)
        continue
    doc = fitz.open(path)
    page = doc[0]
    pix = page.get_pixmap(matrix=fitz.Matrix(ZOOM, ZOOM), alpha=True)  # transparent background
    img = Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGBA")
    if img.width > MAXW:
        h = round(img.height * MAXW / img.width)
        img = img.resize((MAXW, h), Image.LANCZOS)
    outpath = os.path.join(DST, out)
    img.save(outpath, optimize=True)
    print(f"{out}: {img.width}x{img.height} alpha={img.mode}")
    doc.close()
