from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

train_file = client.files.create(
  file=open(r"./data/dataset.jsonl", "rb"),
  purpose="fine-tune"
)

print(train_file)
print("\n")

finetuning_job = client.fine_tuning.jobs.create(
  training_file=train_file.id,
  model=os.environ.get("BASE_MODEL"),
  hyperparameters={
      "n_epochs": 1,
    }
)

print(finetuning_job)

