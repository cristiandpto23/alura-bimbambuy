def create_retriever(vector_store):
    """
    Crea un retriever a partir del índice FAISS.
    """

    return vector_store.as_retriever(
        search_kwargs={"k": 3}
    )