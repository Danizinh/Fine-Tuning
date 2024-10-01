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

                 if count > 10:
                     break
                 count += 1

                 if user and assistant:
                    # Caso não tenha registro em branco, adiciona-o à lista
                    fine_tuning_data.append({
                        "messages": [
                            {"role": "system", "content": "You are an assistant specialized in e-commerce and must provide exactly the product description as stated in the training. Don't give generic answers, just the descriptions provided."},
                            {"role": "user", "content": "Procuct name: " + user},
                            {"role": "assistant", "content": "Product description: " + assistant}
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