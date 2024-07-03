import streamlit as st
import os
from openai import AzureOpenAI

# Initialize Azure OpenAI client
client = AzureOpenAI(
  azure_endpoint = os.getenv("OPENAI_ENDPOINT"), 
  api_key=os.getenv("OPENAI_API_KEY"),  
  api_version="2024-02-15-preview"
)

# Initialize conversation context
conversation_history = []

# Create a Streamlit app
st.title("Azure OpenAI Chatbot")

# Function to display conversation history
def display_history(history):
    for message in history:
        if message["role"] == "user":
            st.text_input("User:", value=message["content"], key=message["content"], disabled=True)
        elif message["role"] == "assistant":
            st.text_input("Assistant:", value=message["content"], key=message["content"], disabled=True)

# Continuous conversation loop
while True:
    user_input = st.text_input("You:", key="user_input")
    if user_input:
        # Create a user message
        user_message = {"role": "user", "content": user_input}
        conversation_history.append(user_message)

        # Generate response from Azure OpenAI
        response = client.chat.completions.create(
            model="gupol01",  # Specify the model identifier
            messages=conversation_history
        )

        # Add assistant's response to context
        assistant_response = response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": assistant_response})

        # Display conversation history
        st.write("Conversation History:")
        display_history(conversation_history)
