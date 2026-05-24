# GenAI Chat Application using LangChain, Ollama & Streamlit

This project is a Generative AI Chat Application built using:

- LangChain
- Ollama
- Streamlit
- Gemma Model

The application allows users to interact with an AI assistant through a simple and interactive web interface.

---

# Features

- Interactive chatbot UI using Streamlit
- Local LLM execution using Ollama
- LangChain prompt chaining
- Environment variable support using dotenv
- LangSmith tracing support
- Lightweight and beginner-friendly GenAI project

---

# Tech Stack

| Technology | Description |
|------------|-------------|
| Python | Programming Language |
| Streamlit | Frontend Web Framework |
| LangChain | LLM Application Framework |
| Ollama | Run Open Source LLMs Locally |
| Gemma | Open-source LLM Model |
| dotenv | Environment Variable Management |

---

# Project Structure

```bash
My-Practice-Python/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
└── .venv/
```

---

# About LangChain

LangChain is a framework used to build applications powered by Large Language Models (LLMs).

It helps developers:
- Create prompt templates
- Build AI chains
- Connect LLMs with external tools
- Manage memory and agents
- Develop GenAI applications easily

Official Website:
https://www.langchain.com/

---

# About Ollama

Ollama allows developers to run open-source Large Language Models locally on their machines.

Benefits:
- No API cost
- Local inference
- Fast experimentation
- Privacy-focused AI applications

Official Website:
https://ollama.com/

---

# About Gemma Model

Gemma is an open-source AI model developed by Google.

In this project, the `gemma:2b` model is used through Ollama for local AI inference.

---

# Create Virtual Environment

## Windows

```bash
python -m venv .venv
```

Activate virtual environment:

```bash
.venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit
pip install langchain
pip install langchain-community
pip install python-dotenv
```

---

# Install Ollama

Download Ollama from:

https://ollama.com/download

After installation, pull the Gemma model:

```bash
ollama pull gemma:2b
```

Run the model:

```bash
ollama run gemma:2b
```

---

# Run the Streamlit Application

```bash
streamlit run app.py
```

Or:

```bash
python -m streamlit run app.py
```

---

# Environment Variables

Create a `.env` file and add:

```env
LANGCHAIN_API_KEY=your_api_key
LANGCHAIN_PROJECT=your_project_name
```

---

# Sample Application Workflow

1. User enters a question
2. Streamlit sends input to LangChain
3. LangChain formats prompt
4. Ollama processes the prompt using Gemma model
5. AI-generated response is displayed to the user

---

# Future Improvements

- Chat history memory
- Multiple LLM support
- PDF Question Answering
- RAG Applications
- Voice Assistant Integration
- Deployment on Cloud

---

# Author

Developed as part of a Generative AI learning project.


#Demo:

<img width="725" height="862" alt="image" src="https://github.com/user-attachments/assets/dfddf659-1e20-4b7d-96ad-d5f9a65696b6" />


---

# License

This project is open-source and available for learning purposes.
