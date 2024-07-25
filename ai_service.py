# ai_service.py
from flask import Flask, request, jsonify
import os
import requests
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')

# Define the base URL for Google AI Studio API
BASE_URL = "https://aistudio.googleapis.com/v1"  # Update with the actual API base URL if different

def generate_content(prompt, api_key):
    """Generate content using Google AI Studio's API."""
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }
    data = {
        "prompt": prompt,
        "maxTokens": 200,  # Adjust parameters as needed
        "temperature": 0.7
    }

    response = requests.post(f"{BASE_URL}/generateText", headers=headers, json=data)
    if response.status_code == 200:
        return response.json().get('content')
    else:
        raise Exception(f"API Error: {response.status_code} - {response.text}")

def moderate_content(content, api_key):
    """Moderate content using Google AI Studio's API."""
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }
    data = {
        "content": content
    }

    response = requests.post(f"{BASE_URL}/moderateText", headers=headers, json=data)
    if response.status_code == 200:
        return response.json().get('result')
    else:
        raise Exception(f"API Error: {response.status_code} - {response.text}")

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.json.get('prompt')
    try:
        generated_content = generate_content(prompt, api_key)
        return jsonify({'content': generated_content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/moderate', methods=['POST'])
def moderate():
    content = request.json.get('content')
    try:
        moderation_result = moderate_content(content, api_key)
        return jsonify({'moderation_result': moderation_result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
