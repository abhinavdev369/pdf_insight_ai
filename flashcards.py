from langchain.llms import OpenAI
import os
from dotenv import load_dotenv
from langchain_community.llms import HuggingFaceHub

load_dotenv()
#llm=OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"),temperature=0.5)

llm=HuggingFaceHub(
    repo_id="gpt2",
    model_kwargs={"temperature":0.3,"max_length":512}
)

def genflash1(text):
    prompt=f"""
Read this content\n{text}
generate 5 flashcards in the format:
Q:....
A:....
"""
    return llm(prompt)

def genflash2(text):
    prompt=f"""
based on content :\n{text}
create 3 multiple choices with 4 option and highlight correct one"""
    return llm(prompt)