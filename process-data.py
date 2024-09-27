import json

# Preparar os dados para fine-tuning
def preparar_dados_para_finetuning(input_file, output_file):
     fine_tuning_data = []
     count = 1

     # Abra o arquivo JSON no formato JSONL
     with open(input_file, 'r') as infile:
         for line in infile:
             try:
                 # Carregar cada linha como um objeto JSON
                 record = json.loads(line)

                 # Extrair os dados que serão usados
                 user = f"{record['title']}"
                 assistant = f"{record['content']}"

                 if count > 100:
                     break
                 count += 1

                 if user and assistant:
                    # Caso não tenha registro em branco, adiciona-o à lista
                    fine_tuning_data.append({
                        "messages": [
                            {"role": "system", "content": "Você é um assistente especializado em e-commerce, responsável por fornecer descrições detalhadas e precisas de produtos com base no nome fornecido."},
                            {"role": "user", "content": "Nome do produto: " + user},
                            {"role": "assistant", "content": "Descrição: " + assistant}
                        ]})
                 

             except json.JSONDecodeError as e:
                 print(f"Erro ao decodificar linha: {line}")
                 print(f"Erro: {e}")

     # Escrever os dados convertidos para um novo arquivo JSONL
     with open(output_file, 'w') as outfile:
         for entry in fine_tuning_data:
             json.dump(entry, outfile)
             outfile.write('\n')

# Arquivo de dados para fine-tuning
input_file = 'data/trn.json'
output_file = 'data/dataset.jsonl'

preparar_dados_para_finetuning(input_file, output_file)