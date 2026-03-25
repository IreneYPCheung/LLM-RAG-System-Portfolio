import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

print("--- DIAGNOSTICS START ---")
if not api_key or len(api_key) < 20:
    print("API Key looks invalid or empty.")
    exit()

if not api_key.startswith("AIza"):
    print("API Key does not start with AIza (Standard Google AI Studio Key).")

# 1. Test List Models
print("\n[Testing List Models API]")
url_list = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
try:
    resp = requests.get(url_list)
    print(f"Status: {resp.status_code}")
    if resp.status_code == 200:
        data = resp.json()
        models = [m['name'] for m in data.get('models', []) if 'generateContent' in m.get('supportedGenerationMethods', [])]
        print(f"Authorized Models for your key: {len(models)} found.")
        print(f"Sample models: {', '.join(models[:5])}")
    else:
        print(f"Error: {resp.text[:500]}")
except Exception as e:
    print(f"Request failed: {e}")

# 2. Test IP Location according to a generic IP checker
print("\n[Testing Current Terminal IP Location]")
try:
    ip_resp = requests.get("https://ipapi.co/json/", timeout=5)
    ip_data = ip_resp.json()
    print(f"Terminal IP Location: {ip_data.get('city')}, {ip_data.get('country_name')}")
    print(f"Terminal IP Org: {ip_data.get('org')}")
except Exception as e:
    print(f"IP Check failed: {e}")

print("--- DIAGNOSTICS END ---")
