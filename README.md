# AI Agent Chatbot

An AI-powered chatbot built with Python that uses LangChain and Groq to generate responses, with optional web search through Tavily. The project provides a FastAPI backend and a Streamlit frontend.

## Features

- **LLM-powered responses:** Uses Groq with the `openai/gpt-oss-120b` model.
- **Optional web search:** Integrates Tavily search to help the agent retrieve web information.
- **FastAPI backend:** Exposes an API endpoint for processing chatbot queries.
- **Streamlit frontend:** Provides a user interface for entering queries, configuring the model provider, and enabling web search.
- **Configurable prompts:** Allows users to supply a system prompt to guide the agent's responses.
- **HTTP error handling:** Includes handling for request timeouts, connection failures, HTTP errors, and other request exceptions.

## Tech Stack

- Python
- FastAPI and Uvicorn
- LangChain
- Groq
- Tavily Search
- Streamlit
- Requests
- Pydantic

## Project Structure

```text
Agentic-ChatBot-FastApi/
├── ai_agent.py
├── backend.py
├── frontend.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Prerequisites

- Python installed on your system
- A Groq API key
- A Tavily API key if you want to use web search

## Setup

1. Clone this repository:

   ```bash
   git clone <YOUR_GITHUB_REPOSITORY_URL>
   cd Agentic-ChatBot-FastApi
   ```

2. Create and activate a virtual environment:

   **Windows PowerShell**

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root:

   ```dotenv
   GROQ_API_KEY=your_groq_api_key
   TAVILY_API_KEY=your_tavily_api_key
   ```

   Replace the placeholders with your own API keys. Keep `.env` private and never commit it to Git.

## Running the Application

Start the FastAPI backend in one terminal:

```powershell
uvicorn backend:app --host 127.0.0.1 --port 9999
```

Open the API documentation at:

`http://127.0.0.1:9999/docs`

Start the Streamlit frontend in a second terminal:

```powershell
streamlit run frontend.py
```

The frontend expects the backend to be available at `http://127.0.0.1:9999`.

## Current Development Status

The project is under development. The current Windows Python 3.14 environment has encountered Windows Application Control blocks affecting compiled Python extensions, including `tiktoken` and `ormsgpack`.

The application has not been verified to start successfully in the current environment. The run instructions above describe the intended workflow and may require dependency or environment troubleshooting.

## Security

- API keys should be stored in a local `.env` file.
- `.env`, virtual environments, Python cache files, and local secret configuration files are excluded through `.gitignore`.
- Never publish API keys, access tokens, passwords, or other private credentials.

## License

No license has been specified yet. All rights remain with the copyright holder unless a license is added.
