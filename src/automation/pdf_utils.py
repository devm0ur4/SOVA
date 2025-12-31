from pypdf import PdfMerger 
from config.paths import DOWNLOAD_DIR, RAW_DIR

def merge_pdfs(output_name="merged.pdf"):
    pdf1 = DOWNLOAD_DIR / "1.pdf"
    pdf2 = DOWNLOAD_DIR / "2.pdf"

    if not pdf1.exists() or not pdf2.exists():
        raise FileNotFoundError("1.pdf ou 2.pdf não encontrados")

    RAW_DIR.mkdir(parents=True, exist_ok=True)

    output_path = RAW_DIR / output_name

    merger = PdfMerger()
    merger.append(str(pdf1))
    merger.append(str(pdf2))

    with open(output_path, "wb") as f:
        merger.write(f)

    merger.close()

## NOTE : TERMINAR ESSA PORRA DEPOIS 
def returnInfo():
    pass
