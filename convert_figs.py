import fitz  # PyMuPDF
from PIL import Image
import io, os

BASE = r"D:/Doctor/paperwriting_exp/2026_boundary_tactile/TEAI_template"
DST = r"C:/Users/XSQ/ViTacMotor/static/images"

# map: source pdf (relative to BASE) -> output png name
figs = {
    "Figure_arxiv/Figure1_arxiv.pdf": "teaser.png",
    "Figure_arxiv/Figure2_arxiv.pdf": "method.png",
    "Figure_arxiv/Figure3_arxiv_1.pdf": "tmc_analysis.png",
    "Figure_new/Figure4_small_1.pdf": "setup.png",
    "Figure_new/Figure_5_exp_3_small.pdf": "qualitative.png",
    "Figure_new/Figure_6_small_2.pdf": "robustness.png",
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
    pix = page.get_pixmap(matrix=fitz.Matrix(ZOOM, ZOOM), alpha=False)
    img = Image.open(io.BytesIO(pix.tobytes("png")))
    if img.width > MAXW:
        h = round(img.height * MAXW / img.width)
        img = img.resize((MAXW, h), Image.LANCZOS)
    outpath = os.path.join(DST, out)
    img.save(outpath, optimize=True)
    print(f"{out}: {img.width}x{img.height}")
    doc.close()
