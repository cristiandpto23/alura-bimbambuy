from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


def load_documents(folder_path: str):
    """
    Carga todos los archivos PDF de una carpeta y devuelve
    una lista de documentos.
    """

    documents = []

    pdf_files = Path(folder_path).glob("*.pdf")

    for pdf in pdf_files:
        loader = PyPDFLoader(str(pdf))
        documents.extend(loader.load())

    return documents