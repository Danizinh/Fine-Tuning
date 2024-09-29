from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt_sistema = """You will receive an Amazon product name that was trained in the fine-tuning and your role is to provide the exact product description from the product name in the input database2 file.
# Output format: 
- Product Name: product name
- Product Description: product description
# Example:
- Product Name: Nice for Mice
- Product Description: Jill Barklem was born in Epping in 1951. After an accident when she was thirteen, Jill was unable to take part in PE or games at school and instead developed her talent for drawing and art. On leaving school, she studied illustration at St Martin's in London. Jill is now a full-time illustrator, working on the series of Brambly Hedge books."""

#prompt_usuario = input("Inform the Amazon Product Name: ")
prompt_usuario = "The Book of Revelation"

pre_completion = client.chat.completions.create(
  model=os.getenv("BASE_MODEL"),
  #max_tokens=250,
  temperature=0.1,
  messages=[
    {"role": "system", "content": prompt_sistema},
    {"role": "user", "content": prompt_usuario}
  ]
)

pos_completion = client.chat.completions.create(
  model=os.getenv("FINE_TUNE_MODEL_v1"),
  #max_tokens=250,
  temperature=0.1,
  messages=[
    {"role": "system", "content": prompt_sistema},
    {"role": "user", "content": prompt_usuario}
  ]
)

# Acessar o conteúdo da resposta
print("\nPRE Fine Tuning:\n")
print(pre_completion.choices[0].message.content)
print("\nPOS Fine Tuning:\n")
print(pos_completion.choices[0].message.content)
print("\nExpected Output: \nProduct Desription: American Baptist pastor, Bible teacher, and writer, Clarence Larkin was born October 28, 1850, in Chester, Delaware County, Pennsylvania. He was converted...")