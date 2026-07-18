from src.document_loader import load_documents
from src.text_splitter import split_documents
from src.vector_store import create_vector_store


documents = load_documents("data/pdfs")

chunks = split_documents(documents)

vector_store = create_vector_store(chunks)

print(f"Documentos cargados: {len(documents)}")
print(f"Chunks creados: {len(chunks)}")

print()

print("Base vectorial creada correctamente.")

results = vector_store.similarity_search(
    "¿Cómo funciona la garantía?",
    k=3
)

for i, result in enumerate(results, start=1):
    print(f"\n===== Resultado {i} =====")
    print(result.metadata)
    print(result.page_content[:500])

