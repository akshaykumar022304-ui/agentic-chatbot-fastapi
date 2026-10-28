# Step 1 : setup UI with Streamllit (model provider, model, web search ,system prompt)

import streamlit as st

st.set_page_config(page_title="LangGraph Agent UI", layout ="centered")
st.title("Ai chatbot Agents")
st.write("Create and Interact with the AI agent")

system_prompt=st.text_area("Define your AI agent", height = 70, placeholder="Type your system prompt here....")

MODEL_NAMES_GROQ=["openai/gpt-oss-120b"]

provider=st.radio("Select Provier :", ("Groq"))

if provider=="Groq":
    selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)

allow_web_search=st.checkbox("Allow web search")

user_query=st.text_area("Enter your query ", height = 150, placeholder="Ask anything....")

API_URL="http://127.0.0.1:9999/chat"

if st.button("Ask agent!"):

    if user_query.strip(): #This removes all the random blank spaces 
        
        # Step 2 : Connect with backend via URL 
        import requests

        payload={    
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }
        response=requests.post(API_URL, json=payload)
        
       
        if response.status_code == 200:
            response_data = response.json()

            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent response")
                st.markdown(f"**Final response:** {response_data}")
        else:
            st.error(f"Request failed: {response.status_code}")
            st.write(response.text)



