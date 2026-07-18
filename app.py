from src.document_loader import load_documents

documents = load_documents("data/pdfs")

print(f"Se cargaron {len(documents)} páginas.\n")

print("Metadata:")
print(documents[0].metadata)

print("\nContenido:")
print(documents[0].page_content[:500])