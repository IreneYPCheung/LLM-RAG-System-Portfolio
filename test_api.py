import os
from dotenv import load_dotenv
import requests

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key or api_key == "your_api_key_here":
    print("API Key is missing or default.")
else:
    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text[:500]}") # Print first 500 chars

    # Try curl equivalent for gemini-1.5-flash
    url_post = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    headers = {'Content-Type': 'application/json'}
    data = '{"contents": [{"parts":[{"text": "Hello"}]}]}'
    
    print("\nTesting Generate Content via HTTP directly:")
    resp_post = requests.post(url_post, headers=headers, data=data)
    print(f"POST Status: {resp_post.status_code}")
    print(f"POST Response: {resp_post.text[:500]}")
