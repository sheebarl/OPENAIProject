import os
from openai import AzureOpenAI


client = AzureOpenAI(
  azure_endpoint = os.getenv("OPENAI_ENDPOINT"), 
  api_key=os.getenv("OPENAI_API_KEY"),  
  api_version="2023-05-15"
)

response = client.chat.completions.create(
    model="gupol01",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "what is Python language?"},
        {"role": "assistant", "content": "Python is a interpreter language."},
        {"role": "user", "content": "what are the other features of python language?"}
    ]
)

#print(response)
print(response.choices[0].message.content)


