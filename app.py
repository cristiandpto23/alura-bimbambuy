from src.document_loader import load_documents
from src.text_splitter import split_documents

documents = load_documents("data/pdfs")

chunks = split_documents(documents)

print(f"Documentos cargados: {len(documents)}")
print(f"Chunks creados: {len(chunks)}")

print("\nPrimer chunk:\n")

print(chunks[0].page_content)