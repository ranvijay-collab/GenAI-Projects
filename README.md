LangChain LangServe FastAPI Translation API

A simple REST API built using LangChain, LangServe, FastAPI, and Groq LLMs. This project demonstrates how to expose a LangChain Expression Language (LCEL) chain as an API endpoint using LangServe.

🚀 Features
FastAPI-based web server
LangChain Expression Language (LCEL)
LangServe integration for serving chains as APIs
Groq LLM integration
Dynamic language translation
Auto-generated API documentation
Ready for deployment and testing
🛠️ Tech Stack
Python
FastAPI
LangChain
LangServe
Groq API
Uvicorn
Python Dotenv
📂 Project Structure
.
├── app.py
├── .env
├── requirements.txt
├── README.md
└── ...
⚙️ Installation
1. Clone the Repository
git clone <repository-url>
cd GenAI-Projects
2. Create Virtual Environment
conda create -n langserve python=3.11
conda activate langserve
3. Install Dependencies
pip install -r requirements.txt
🔑 Environment Variables

Create a .env file in the project root directory.

GROQ_API_KEY=your_groq_api_key

Note: Never commit your .env file or API keys to GitHub.

🧠 Application Workflow
User sends text and target language.
LangChain Prompt Template formats the request.
Groq LLM processes the translation.
Output Parser extracts the response.
LangServe exposes the chain as a REST API endpoint.
Chain Architecture
User Input
     │
     ▼
ChatPromptTemplate
     │
     ▼
ChatGroq Model
     │
     ▼
StrOutputParser
     │
     ▼
Translated Output
▶️ Running the Application

Start the FastAPI server:

python app.py

or

uvicorn app:app --reload

Server will run at:

http://127.0.0.1:8000
🌐 API Endpoints
LangServe Playground
http://127.0.0.1:8000/chain/playground/
Invoke Endpoint
POST /chain/invoke

Example Request:

{
  "input": {
    "language": "French",
    "text": "How are you?"
  }
}

Example Response:

{
  "output": "Comment allez-vous ?"
}
📖 API Documentation

FastAPI automatically generates API documentation.

Swagger UI:

http://127.0.0.1:8000/docs

ReDoc:

http://127.0.0.1:8000/redoc
📦 Required Packages
pip install fastapi
pip install uvicorn
pip install langchain
pip install langchain-core
pip install langchain-groq
pip install langserve
pip install python-dotenv
🎯 Learning Objectives

This project demonstrates:

LangChain LCEL chains
Prompt engineering
Groq LLM integration
LangServe deployment
FastAPI integration
REST API development for Generative AI applications
🔒 Security Note
Store API keys in .env files.
Add .env to .gitignore.
Rotate API keys if they are accidentally exposed.
Never hardcode secrets in source code.
📜 License

This project is intended for educational and learning purposes.
