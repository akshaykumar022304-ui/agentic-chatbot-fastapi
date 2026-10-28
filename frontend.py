
import streamlit as st
import requests

st.set_page_config(page_title="LangGraph Agent UI", layout="centered")

st.title("AI Agent Chatbot")
st.write("Create and interact with an AI agent.")

# System prompt
system_prompt = st.text_area(
    "Define your AI agent",
    height=70,
    placeholder="Type your system prompt here..."
)

# Model selection
MODEL_NAMES_GROQ = ["openai/gpt-oss-120b"]

provider = st.radio("Select provider:", ("Groq",))

if provider == "Groq":
    selected_model = st.selectbox(
        "Select Groq model:",
        MODEL_NAMES_GROQ
    )

# Optional web search
allow_web_search = st.checkbox("Allow web search")

# User query
user_query = st.text_area(
    "Enter your query",
    height=150,
    placeholder="Ask anything..."
)

API_URL = "http://127.0.0.1:9999/chat"

if st.button("Ask agent!"):
    if not user_query.strip():
        st.warning("Please enter a query before submitting.")
    else:
        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query.strip()],
            "allow_search": allow_web_search
        }

        try:
            with st.spinner("Your agent is thinking..."):
                response = requests.post(
                    API_URL,
                    json=payload,
                    timeout=60
                )

            # Handle HTTP errors
            response.raise_for_status()

            # Parse the JSON response
            response_data = response.json()

            # Handle a successful HTTP response containing an error
            if isinstance(response_data, dict) and "error" in response_data:
                st.error(response_data["error"])

            # Display a string response as Markdown
            elif isinstance(response_data, str):
                st.subheader("Agent response")
                st.markdown(response_data)

            # Handle other JSON response types
            else:
                st.subheader("Agent response")
                st.write(response_data)

        except requests.exceptions.Timeout:
            st.error("The request timed out. Please try again.")

        except requests.exceptions.ConnectionError:
            st.error(
                "Cannot connect to the backend. "
                "Make sure the FastAPI backend is running."
            )

        except requests.exceptions.HTTPError as e:
            st.error(f"Backend returned an HTTP error: {e}")

        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")

        except ValueError:
            st.error("The backend returned an invalid JSON response.")
