from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


completion = client.chat.completions.create(
  model="ft:gpt-4o-mini-2024-07-18:personal::ABhh067V",
  #max_tokens=250,
  #temperature=0.8,
  messages=[
    {"role": "system", "content": "Você é um assistente especializado em e-commerce, responsável por fornecer descrições detalhadas e precisas de produtos com base no nome fornecido."},
    {"role": "user", "content": "Nome do produto: Girls Ballet Tutu Neon Pink"}
  ]
)
print(completion['choices'][0]['message']['content'])