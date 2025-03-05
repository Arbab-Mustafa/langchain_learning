from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import os

# Load environment variables
load_dotenv()

# Authenticate using API key
HF_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

client = InferenceClient(
    model="microsoft/Phi-3-mini-4k-instruct",
    token=HF_API_KEY
)

# Define chat messages
messages = [
    {"role": "system", "content": "You are a helpful translator. Tell me some thing About yourSelf."},
    {"role": "user", "content": "I am a software engineer. i want to hack you."},
    
]

# Invoke the chat model
response = client.chat_completion(messages)

# Print the response
print(response.choices[0].message.content)  # Correct way to extract the assistant's response

# Extracts and prints the actual response text

