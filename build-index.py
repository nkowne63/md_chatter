from pathlib import Path
from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex
from dotenv import load_dotenv

load_dotenv(override=True)

documents = SimpleDirectoryReader('data').load_data()

index = GPTSimpleVectorIndex(documents)

index.save_to_disk("index.json")
