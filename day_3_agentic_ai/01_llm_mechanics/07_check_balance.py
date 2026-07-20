import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

data = requests.get("https://openrouter.ai/api/v1/credits",
                    headers={"Authorization": f"Bearer {os.environ.get('OPENROUTER_API_KEY')}"},
                    timeout=10).json()["data"]

print(f"Total credits: ${data['total_credits']:.4f}")
print(f"Used credits: ${data['total_usage']:.4f}")
print(f"Remaining credits: ${data['total_credits'] - data['total_usage']:.4f}")