import streamlit as st
from pdf_utils import extract_text_from_pdf
from qa_engine import split_text,createvector,summarize_text,ask_ques
from flashcards import genflash1,genflash2
import tempfile

st.set_page_config( page_title="Smart Research Companion",layout="wide"
)
st.title("Smart Research Companion")

file=st.file_uploader("pdfhere",type=["pdf"])

if file:
    with tempfile.NamedTemporaryFile(delete=False,suffix=".pdf") as tmp_file:
        tmp_file.write(file.read())
        pdf_text=extract_text_from_pdf(tmp_file.name)
    
    st.subheader("Extracted text in subheader")
    st.text_area("extracted text",pdf_text[:2000],height=200)
    chunks=split_text(pdf_text)
    vector_store=createvector(chunks)

    st.subheader("ask question in subheader for retreival qa")
    question=st.text_input("ask anything from the pdf")
    if question:
        answer=ask_ques(vector_store,question)
        st.success(answer)
    
    if st.button("summarize text"):
        summary=summarize_text(pdf_text[:3000])
        st.success(summary)
        st.info(summary)
    if st.button("generate flashcards"):
        flashcard=genflash1(pdf_text[:1000])
        st.success(flashcard)
        st.write(flashcard)
    if st.button("generate mcq flashcard"):
        flashcard=genflash2(pdf_text[:1000])
        st.success(flashcard)
        st.write(flashcard)
 