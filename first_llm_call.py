
from dotenv import load_dotenv
from openai import OpenAI
import os

# Read variables from the local .env file
load_dotenv()

# Read the secret key without displaying it
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("OPENAI_API_KEY is missing. Check your .env file.")

# Create the API client
client = OpenAI(api_key=api_key)

# Send a prompt to the model
response = client.responses.create(
    model="gpt-5.5",
    input="Explain Generative AI in simple terms in three bullet points."
)

# Display the generated answer
print(response.output_text)
