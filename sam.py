from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

completion = client.chat.completions.create(
  model="ft:gpt-3.5-turbo-0125:personal::AC4CqQDh",
  #max_tokens=250,
  #temperature=0.8,
  messages=[
   {"role": "system", "content": "You are an e-commerce assistant, and your role is to provide the exact product description."},
    {"role": "user", "content": "Product name: Mog's Kittens"}
  ]
)

# Acessar o conteúdo da resposta
print(completion.choices[0].message)