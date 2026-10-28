#Step1 : Setup API Keys for groq and Taily AND OpenAI
import os 

from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import AIMessage
from rich.console import Console
from rich.markdown import Markdown

GROQ_API_KEY= os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY= os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY= os.environ.get("OPENAI_API_KEY")

#Step2 : Setup LLM and Tools 
from langchain_groq import ChatGroq
# from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

#openai_llm=ChatOpenAI(model="gpt-4o-mini")
#groq_llm=ChatGroq(model="openai/gpt-oss-120b")

search_tool = TavilySearch(max_results=2)

#Step3 : Setup AI Ageb=nt with Search tool functioality 
from langchain.agents import create_agent
from langchain_core.messages.ai import AIMessage


system_prompt="Act as an AI chatbot who is smart and friendly"

def get_response_from_ai_agent(llm_id, query, allow_search , system_prompt, provider):

    if provider == "Groq":
        llm = ChatGroq(model=llm_id)

    elif provider == "OpenAI":
        from langchain_openai import ChatOpenAI
        llm = ChatOpenAI(model=llm_id)

    else:
        raise ValueError(f"Unsupported provider: {provider}")

    tools = [TavilySearch(max_results=2)] if allow_search else[]

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=system_prompt
    )

    state = {
        "messages": [
            {"role": "user", "content": query}
        ]
    }
    response = agent.invoke(state)

    messages = response.get("messages", [])

    # Keep AI messages that are not tool-call requests
    ai_messages = [
        message
        for message in messages
        if isinstance(message, AIMessage) and not message.tool_calls
    ]

    if ai_messages:
        return ai_messages[-1].content
    else:
        return "No final AI response found."