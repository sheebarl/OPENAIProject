import os
import streamlit as st
import openai
from openai import AzureOpenAI

def authenticate(username, password):
    if username == 'xnaish' and password == 'Verma2009!':
        return True
    else:
        return False

# Setting page title, header, and sidebar
st.set_page_config(page_title="Custom ChatGPT", page_icon="💬")
st.markdown("<h1 style='text-align: center;'> A custom ChatGPT 😬</h1>", unsafe_allow_html=True)
st.markdown("Welcome to the custom ChatGPT app. Please log in to continue.")

# # Configure Azure OpenAI API
# openai.api_type = "azure"
# openai.api_base = os.getenv("OPENAI_ENDPOINT")
# openai.api_version = "2023-05-15"
# openai.api_key = os.getenv("OPENAI_API_KEY")

client = AzureOpenAI(
  azure_endpoint = os.getenv("OPENAI_ENDPOINT"), 
  api_key=os.getenv("OPENAI_API_KEY"),  
  api_version="2024-02-15-preview"
)


# Initialize session state variables
if 'is_logged_in' not in st.session_state:
    st.session_state['is_logged_in'] = False
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
if 'model_name' not in st.session_state:
    st.session_state['model_name'] = []

# Sidebar - let user choose model, show total cost of current conversation, and let user clear the current conversation
st.sidebar.title("Your Custom ChatGPT")

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if st.sidebar.button("Login"):
    if authenticate(username, password):
        st.session_state['is_logged_in'] = True
        st.sidebar.success("Logged in successfully")

model_name = st.sidebar.radio("Choose a model:", ("GPT-3.5", "GPT-4"))
counter_placeholder = st.sidebar.empty()
clear_button = st.sidebar.button("Clear Conversation", key="clear")

# Map model names to OpenAI model IDs
if model_name == "GPT-3.5":
    model = "gpt-35-turbo"
else:
    model = "gpt-4"

# Reset everything
if clear_button:
    st.session_state['generated'] = []
    st.session_state['past'] = []
    st.session_state['messages'] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    st.session_state['model_name'] = []

# Generate a response
def generate_response(prompt):
    st.session_state['messages'].append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="gupol01",
        messages=st.session_state['messages'],
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None)
    
    reply = response.choices[0].message.content
    st.session_state['messages'].append({"role": "assistant", "content": reply})

    return reply

if st.session_state['is_logged_in']:
    user_input = st.text_area("You:")
    if user_input:
        output = generate_response(user_input)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)
        st.session_state['model_name'].append(model_name)

    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            st.text(f"You: {st.session_state['past'][i]}")
            st.text(f"Assistant: {st.session_state['generated'][i]}")
            st.write(f"Model used: {st.session_state['model_name'][i]}")