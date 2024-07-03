import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_type = 'azure'
openai.api_base = os.getenv("OPENAI_ENDPOINT")
openai.api_version = "2023-09-15-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

deploymentName= "gupol01"

user_prompt = "What is Python language?"

response=openai.Completion.create(engine=deploymentName, prompt=user_prompt, max_tokens=10)

print(response)

# response = openai.Completion.create(
#   engine="gupol01",
#   prompt="",
#   temperature=1,
#   max_tokens=100,
#   top_p=0.5,
#   frequency_penalty=0,
#   presence_penalty=0,
#   best_of=1,
#   stop=None)
