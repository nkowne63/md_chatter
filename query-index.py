import os
from llama_index import GPTSimpleVectorIndex
from dotenv import load_dotenv

load_dotenv(override=True)

query = os.getenv('QUERY_STRING')

index = GPTSimpleVectorIndex.load_from_disk("index.json")

response = index.query(query)
print(response)
