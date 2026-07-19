# 🤖 BimBam Buy AI Assistant

Asistente inteligente basado en **Retrieval-Augmented Generation (RAG)** capaz de responder preguntas en lenguaje natural utilizando la documentación oficial de **BimBam Buy** como fuente de conocimiento.

El proyecto fue desarrollado como parte del **Challenge ONE Oracle + Alura**, utilizando Python, LangChain, FAISS, Google Gemini y Streamlit.

---

# 🚀 Características

- Lectura automática de documentos PDF.
- División inteligente del contenido en fragmentos (chunks).
- Generación de embeddings mediante Sentence Transformers.
- Almacenamiento vectorial utilizando FAISS.
- Recuperación semántica de información mediante Retriever.
- Generación de respuestas utilizando Google Gemini.
- Interfaz web desarrollada con Streamlit.

---

# 🏗 Arquitectura

```text
Usuario
    │
    ▼
Streamlit
    │
    ▼
Agent
    │
    ├── Document Loader
    ├── Text Splitter
    ├── Vector Store (FAISS)
    ├── Retriever
    └── Gemini
```

---

# 🛠 Tecnologías utilizadas

- Python 3.12
- Streamlit
- LangChain
- Google Gemini
- FAISS
- Sentence Transformers
- PyPDF
- Python Dotenv

---

# 📁 Estructura del proyecto

```text
bimbambuy-ai-assistant/

├── app.py
├── app_console.py
├── README.md
├── requirements.txt
├── .env.example
│
├── data/
│   └── pdfs/
│
└── src/
    ├── agent.py
    ├── document_loader.py
    ├── text_splitter.py
    ├── vector_store.py
    ├── retriever.py
    ├── llm.py
    └── prompts.py
```

---

# ⚙ Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/TU-USUARIO/bimbambuy-ai-assistant.git
```

## 2. Crear un entorno virtual

```bash
python -m venv .venv
```

## 3. Activar el entorno

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

## 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# 🔑 Configuración

Crear un archivo `.env` en la raíz del proyecto.

```env
GOOGLE_API_KEY=TU_API_KEY
GEMINI_MODEL=gemini-3.1-flash-lite
```

---

# ▶ Ejecutar la aplicación

```bash
streamlit run app.py
```

---

# 💬 Ejemplos de preguntas

- ¿Cómo funciona la garantía?
- ¿Cuál es la política de reembolsos?
- ¿Qué métodos de pago acepta BimBam Buy?
- ¿Cómo funciona el programa de afiliados?

---

# 🧠 Arquitectura RAG

```text
PDFs

↓

Document Loader

↓

Text Splitter

↓

Embeddings

↓

FAISS

↓

Retriever

↓

Gemini

↓

Respuesta
```

---

# 🔮 Mejoras futuras

- Persistencia del índice FAISS.
- Soporte para múltiples documentos.
- Historial de conversaciones.
- Citas automáticas indicando el documento fuente.
- Carga dinámica de documentos desde la interfaz.

---

# 👨‍💻 Autor

Cristian
Challenge ONE Oracle Next Education + Alura 