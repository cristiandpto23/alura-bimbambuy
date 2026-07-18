from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from src.prompts import SYSTEM_PROMPT
import os

load_dotenv()

def create_llm():
    """
    Crea la instancia del modelo Gemini.
    """
    
    model = os.getenv("GEMINI_MODEL")

    llm = ChatGoogleGenerativeAI(
        model=model,
        temperature=0
    )

    return llm


def generate_answer(llm, question, context):
    """
    Genera una respuesta utilizando el contexto recuperado.
    """

    prompt = f"""
{SYSTEM_PROMPT}

Contexto:

{context}

Pregunta:

{question}
"""

    response = llm.invoke(prompt)

    if isinstance(response.content, list):
        return "".join(
            block["text"]
            for block in response.content
            if isinstance(block, dict) and "text" in block
        )

    return response.content