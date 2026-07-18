from src.document_loader import load_documents
from src.text_splitter import split_documents
from src.vector_store import create_vector_store
from src.retriever import create_retriever
from src.llm import create_llm, generate_answer


def create_agent():
    """
    Inicializa el agente RAG.
    """

    documents = load_documents("data/pdfs")
    chunks = split_documents(documents)
    vector_store = create_vector_store(chunks)

    retriever = create_retriever(vector_store)

    llm = create_llm()

    return retriever, llm


def ask_question(retriever, llm, question):
    """
    Responde una pregunta utilizando el agente RAG.
    """

    results = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in results
    )

    return generate_answer(
        llm=llm,
        question=question,
        context=context
    )