from pypdf import PdfWriter, PdfReader
import re
from config.paths import DOWNLOAD_DIR, RAW_DIR

def merge_pdfs(output_name="merged.pdf"):
    pdf1 = DOWNLOAD_DIR / "1.pdf"
    pdf2 = DOWNLOAD_DIR / "2.pdf"

    if not pdf1.exists() or not pdf2.exists():
        raise FileNotFoundError("1.pdf ou 2.pdf não encontrados")

    RAW_DIR.mkdir(parents=True, exist_ok=True)

    output_path = RAW_DIR / output_name

    merger = PdfWriter()
    merger.append(str(pdf1))
    merger.append(str(pdf2))

    with open(output_path, "wb") as f:
        merger.write(f)

    merger.close()

## NOTE : TERMINAR ESSA PORRA DEPOIS 
def read_pdf(pdf_path: str):
    reader = PdfReader(pdf_path)

    texto = ""
    for page in reader.pages:
        texto += page.extract_text() + "\n"

    # Data de emissão (dd/mm/yyyy)
    data_emissao = re.search(r"\b(\d{2}/\d{2}/\d{4})\b", texto)
    data_emissao = data_emissao.group(1) if data_emissao else None

    # Valor total da nota fiscal
    valor_match = re.search(
        r"VALOR TOTAL DA NOTA FISCAL:\s*R\$\s*([\d\.,]+)",
        texto
    )

    valor_total = None
    if valor_match:
        valor_total = float(
            valor_match.group(1)
            .replace(".", "")
            .replace(",", ".")
        )

    return {
        "data_emissao": data_emissao,
        "valor_total": valor_total
    }
