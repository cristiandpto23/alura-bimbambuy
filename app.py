from src.agent import create_agent, ask_question

retriever, llm = create_agent()

question = "¿Cómo funciona la garantía?"

answer = ask_question(
    retriever,
    llm,
    question
)

print(answer)

