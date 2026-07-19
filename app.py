import streamlit as st

from src.agent import create_agent, ask_question


st.set_page_config(
    page_title="BimBam Buy AI Assistant",
    page_icon="🤖"
)


@st.cache_resource
def load_agent():
    return create_agent()


retriever, llm = load_agent()

st.title("🤖 BimBam Buy AI Assistant")

st.write(
    "Haz preguntas sobre la documentación oficial de BimBam Buy."
)

question = st.text_input(
    "Escribe tu pregunta:"
)

if st.button("Preguntar"):

    if question.strip():

        with st.spinner("Buscando respuesta..."):

            answer = ask_question(
                retriever,
                llm,
                question
            )

        st.subheader("Respuesta")

        st.write(answer)

    else:
        st.warning("Por favor, escribe una pregunta.")