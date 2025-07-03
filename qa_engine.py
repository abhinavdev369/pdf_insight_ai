import os
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.chains import retrieval_qa

load_dotenv()
open_ai_key=os.getenv("OPENAI_API_KEY")

llm=OpenAI(openai_api_key=open_ai_key,temperature=0.3)

def split_text(text):
    splitter=CharacterTextSplitter(chunk_size=1000,chunk_overlap=150)
    return splitter.split_text(text)

def createvector(chunks):
    embed=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-V2")
    return FAISS.from_texts(chunks,embedding=embed)

def ask_ques(vector_store,question):

    retreiver=vector_store.as_retreiver()
    qa=retrieval_qa.from_chain_type(llm=llm,retreiver=retreiver)
    return qa.run(question)

def summarize_text(text):
    prompt=f"Summarize it in simple terms"
    return llm(prompt)

