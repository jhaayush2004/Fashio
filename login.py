import os
from huggingface_hub import HfApi

# Set your Hugging Face API token here
os.environ['HF_API_TOKEN'] = os.getenv('HF_API_TOKEN')

# Create an instance of the API
api = HfApi()

# Check that the token is valid
user_info = api.whoami()
print(user_info)
