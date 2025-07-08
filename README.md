# 📚 PDF Insight AI

*Smart Research Companion* powered by OpenAI and Hugging Face — designed to help you interact with your PDFs using AI.

👉 Live Demo: [https://pdfinsightai.streamlit.app/](https://pdfinsightai.streamlit.app/)

---

## 🚀 Features

- 📄 *PDF Text Extraction*
- 🧠 *Text Summarization* (OpenAI/Hugging Face powered)
- ❓ *Ask Questions about PDF Content*
- 🃏 *Flashcard Generation*
- 🎯 *MCQ-Style Flashcard Creation*
- ☁ *Deployed on Streamlit Cloud*

---

## 🛠 Tech Stack

- *Frontend:* Streamlit
- *LLMs:* OpenAI GPT-3.5 / Hugging Face (Falcon, T5, etc.)
- *Vector Store:* FAISS
- *Text Processing:* LangChain, PyMuPDF
- *Deployment:* Streamlit Cloud

---

## 📌 How It Works

1. Upload a PDF.
2. Text is extracted and chunked using LangChain.
3. Vector embeddings are created using OpenAI or Hugging Face models.
4. You can:
   - Ask questions from the PDF (Vector Search)
   - Generate a summary of the content
   - Create flashcards or MCQs automatically

---

## ⚙ Setup Locally

### Clone the repository

```bash
git clone https://github.com/abhinavdev369/pdf_insight_ai.git
cd pdf_insight_ai
pip install -r requirements.txt
OPENAI_API_KEY = "your-openai-key"
HUGGINGFACEHUB_API_TOKEN = "your-huggingfacehub-key"
streamlit run app.py
