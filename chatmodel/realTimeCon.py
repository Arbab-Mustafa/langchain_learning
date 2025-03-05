from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

HF_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

client = InferenceClient(
    api_key=HF_API_KEY  # No need to specify provider here
)

result = client.text_generation(
    model="microsoft/phi-2",
    prompt="Can you please let us know more details about your "
)

print(result)
