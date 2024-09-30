## Fine-Tuning de um Foundation Model

No Tech Challenge desta fase, você precisa executar o fine-tuning de um foundation model (Llama, BERT, MISTRAL etc.), utilizando o dataset "The AmazonTitles-1.3MM". O modelo treinado deverá:

- Receber perguntas com um contexto obtido por meio do arquivo JSON “trn.json” que está contido dentro do dataset.
- A partir do prompt formado pela pergunta do usuário sobre o título do produto, o modelo deverá gerar uma resposta baseada na pergunta do usuário trazendo como resultado do aprendizado do fine-tuning os dados da sua descrição.

## ⚙️ Preparação do Dataset:

1. **Descrição**: O The AmazonTitles-1.3MM consiste em consultas textuais reais de usuários e títulos associados de produtos relevantes encontrados na Amazon e suas descrições, medidos por ações implícitas ou explícitas dos usuários.
2. **Preparação do Dataset**: Faça o download do dataset AmazonTitles-1.3MM e utilize o arquivo “trn.json”. Nele, você utilizará as colunas “title” e “content”, que contêm título e descrição, respectivamente. Prepare os prompts para o fine-tuning garantindo que estejam organizados de maneira adequada para o treinamento do modelo escolhido. Limpe e pré-processe os dados conforme necessário para o modelo escolhido.
3. **Chamada do Foundation Model**: Importe o foundation model que será utilizado e faça um teste apresentando o resultado atual do modelo antes do treinamento (para que se obtenha uma base de análise após o fine-tuning), e então será possível avaliar a diferença do resultado gerado.
4. **Execução do Fine-Tuning**: Execute o fine-tuning do foundation model selecionado (por exemplo, BERT, GPT, Llama) utilizando o dataset preparado. Documente o processo de fine-tuning, incluindo os parâmetros utilizados e qualquer ajuste específico realizado no modelo.
5. **Geração de Respostas**: Configure o modelo treinado para receber perguntas dos usuários. O modelo deverá gerar uma resposta baseada na pergunta do usuário e nos dados provenientes do fine-tuning, incluindo as fontes fornecidas.

## Fine-Tuning usando a OpenAI:

### Etapas:

1. **gpt-database-v2.py** -> Realiza a etapa de preparação da base de dados extraindo "title" e "content" e diminuindo a quantidade de linhas devido a recursos limimtados.
2. **gpt-finetuning-v2.py** -> Chama a API da OpenAI para realizar o Fine-Tuning do modelo base (gpt-4o-mini) utilizando a base de dados ./data/dataset2.jsonl.
3. **gpt-prompt-v2.py** -> Realiza a interação com o usuário comparando a resposta do modelo base versus o modelo Fine-Tunned. Os modelos estão em um arquivo .env e o resultado pode ser verificado no **relatório** e **vídeo** do grupo.

### Pré-requisitos

- Python 3.x
- Bibliotecas: `pandas`, `torch`, `transformers`, `bitsandbytes`, `folium`, `huggingface_hub`, `openai`

### Instalação

Instale as bibliotecas necessárias:

```bash
pip install torch

### Execução

```bash
python fine_tune_Tech_challenge_ipynb
```

