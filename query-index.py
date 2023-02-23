import os
from llama_index import GPTTreeIndex, SimpleDirectoryReader, MockLLMPredictor
from dotenv import load_dotenv

load_dotenv()

index = GPTTreeIndex.load_from_disk("index.json")

response = index.query(os.getenv('QUERY_STRING'))
print(response)
