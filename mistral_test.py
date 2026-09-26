from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")

response = requests.post(
    "https://api.mistral.ai/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    },
    json={
        "model": "mistral-small-latest",
        "messages": [
            {
                "role": "user",
                "content": "Give me one short sentence about artificial intelligence."
            }
        ],
        "temperature": 0.2,
    },
    timeout=30,
)

print("STATUS:", response.status_code)
print("BODY:", response.text)