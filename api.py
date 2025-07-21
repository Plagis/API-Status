import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_URL = "https://janice.e-351.com/api/rest/v2/pricer?market=2"
API_KEY = os.getenv("API_KEY")  # get the API key from .env

headers = {
    "accept": "application/json",
    "X-ApiKey": API_KEY,
    "content-Type": "text/plain"
}

data = {"market": 2}

try:
    response = requests.post(API_URL, headers=headers, json=data)
    response.raise_for_status()  # Raises an exception for 4xx and 5xx errors

    # Handle the response if successful
    print(response.json())

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    print(f"Response content: {response.text}")  # Print the error response

