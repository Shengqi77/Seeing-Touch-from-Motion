import fitz  # PyMuPDF
import os

SRC = r"D:/Doctor/paperwriting_exp/2026_boundary_tactile/Paper_2026_ECCV_only_tactile/paper-template-Latest/paper-template-Latest/Figure_new"
DST = r"C:/Users/XSQ/ViTacMotor/static/images"

# map: source pdf -> output png name
figs = {
    "Figure1_small_3.pdf": "teaser.png",
    "Figure2_small.pdf": "method.png",
    "Figure3_samll_1.pdf": "tmc_analysis.png",
    "Figure4_small_1.pdf": "setup.png",
    "Figure_5_exp_3_small.pdf": "qualitative.png",
    "Figure_6_small_2.pdf": "robustness.png",
}

ZOOM = 3.0  # ~216 DPI, crisp for web

for src, out in figs.items():
    path = os.path.join(SRC, src)
    if not os.path.exists(path):
        print("MISSING", path)
        continue
    doc = fitz.open(path)
    page = doc[0]
    mat = fitz.Matrix(ZOOM, ZOOM)
    pix = page.get_pixmap(matrix=mat, alpha=False)
    outpath = os.path.join(DST, out)
    pix.save(outpath)
    print(f"{out}: {pix.width}x{pix.height}")
    doc.close()
