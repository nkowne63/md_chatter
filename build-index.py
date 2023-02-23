from llama_index import GPTTreeIndex, SimpleDirectoryReader, MockLLMPredictor
from dotenv import load_dotenv

load_dotenv()

documents = SimpleDirectoryReader('data').load_data()
index = GPTTreeIndex(documents)
index.save_to_disk("index.json")
