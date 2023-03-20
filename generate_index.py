from gpt_index import GPTKeywordTableIndex, SimpleDirectoryReader, LLMPredictor, PromptHelper
from langchain import OpenAI
from dotenv import load_dotenv
import os
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# set maximum input size
max_input_size = 4096
# set number of output tokens
num_outputs = 256
#set maximum chunk overlap
max_chunk_overlap = 20
# set chunk size limit
chunk_size_limit = 512

# define LLM
llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.7, model_name="text-davinci-003", max_tokens=num_outputs))
prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

documents = SimpleDirectoryReader('data').load_data()

index = GPTKeywordTableIndex(
    documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper
)

# save to disk
index.save_to_disk('index.json')
