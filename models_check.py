from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")

response = requests.get(
    "https://api.mistral.ai/v1/models",
    headers={
        "Authorization": f"Bearer {api_key}"
    }
)

print("STATUS:", response.status_code)

for model in response.json()["data"]:
    print(model["id"])