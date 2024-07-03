import streamlit as st

# Your existing code for Azure OpenAI setup and chat interaction

import os
from openai import AzureOpenAI


client = AzureOpenAI(
  azure_endpoint = os.getenv("OPENAI_ENDPOINT"), 
  api_key=os.getenv("OPENAI_API_KEY"),  
  api_version="2024-02-15-preview"
)



# Create a Streamlit app
st.title("Azure OpenAI Chatbot")
user_input = st.text_input("Ask a question:")

if user_input:
    # Use the user input to create a user message
    user_message = {"role": "user", "content": user_input}
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        user_message
    ]

    # Call the Azure OpenAI API to generate a response
    response = client.chat.completions.create(
        model="",
        messages=messages
    )

    # Display the assistant's response
    st.write("Assistant's Response:")
    st.write(response.choices[0].message.content)
