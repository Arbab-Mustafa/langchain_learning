from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Authenticate using API key
HF_API_KEY = os.getenv("HUGGINGFACE_API_KEY")


# img to txt

client = InferenceClient(
    model="Salesforce/blip-image-captioning-base",
    token=HF_API_KEY
)

# Define image path
# image_path = "./4 - Copy (2) - Copy.png"
image_path= "./Screenshot 2025-03-04 001723.png"
# Invoke the image to text model
response = client.image_to_text(image_path)

# Print the response
print(response.generated_text  )  # Correct way to extract the assistant's response

