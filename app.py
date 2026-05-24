import streamlit as st
import os

from dotenv import load_dotenv

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# LangSmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the question asked"),
        ("user", "Question: {question}")
    ]
)

# Ollama model
llm = Ollama(model="gemma:2b")

# Output Parser
output_parser = StrOutputParser()

# Chain
chain = prompt | llm | output_parser

# Streamlit UI
st.title("LangChain Demo With Gemma Model")

input_text = st.text_input("What is on your mind?")

if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)