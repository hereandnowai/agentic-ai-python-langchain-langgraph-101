import os  # lets us read settings from the computer, like secret keys
import requests  # brings in a tool for fetching information from websites
from dotenv import load_dotenv  # brings in a helper that reads a hidden settings file

load_dotenv()  # Load environment variables from .env file

data = requests.get("https://openrouter.ai/api/v1/credits",  # asks the service how much money is left on the account
                    headers={"Authorization": f"Bearer {os.environ.get('OPENROUTER_API_KEY')}"},
                    timeout=10).json()["data"]

print(f"Total credits: ${data['total_credits']:.4f}")  # shows the total money that was on the account
print(f"Used credits: ${data['total_usage']:.4f}")  # shows how much money has been spent so far
print(f"Remaining credits: ${data['total_credits'] - data['total_usage']:.4f}")  # shows the money still left by subtracting spent from total