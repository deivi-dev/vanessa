import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")

def generate_response(prompt):
        response = requests.post(
            f"{API_URL}/generate-text", 
            json = {"prompt": prompt},
            timeout=60,
        )

        response.raise_for_status()
        return response.json()