from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Authenticate using API key
HF_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

client = InferenceClient(
	provider="nebius",
	api_key=HF_API_KEY
)

# output is a PIL.Image object
image = client.text_to_image(
	"My friend is Ramzan. He is a good programmer. He is a good person. He is on fasting but waiting for iftar also watching Food ",
	model="black-forest-labs/FLUX.1-dev"
)


# Save the image in data folder in current directory & use dynamic name each Time 
image.save("data/Output.png")
print("Image saved successfully")  # Correct way to extract the assistant's response




