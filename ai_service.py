# ai_service.py
from flask import Flask, request, jsonify
from transformers import pipeline
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')

# Load the Gemini model with API key if required
# (The actual implementation of the Gemini model might differ based on the API provider)

# Example placeholder function for authentication, replace with actual usage
def authenticate_model(api_key):
    # Placeholder logic for authenticating the model with the API key
    pass

authenticate_model(api_key)

content_generator = pipeline('text-generation', model='gemini-model')
content_moderator = pipeline('text-classification', model='gemini-model-moderation')

@app.route('/generate', methods=['POST'])
def generate_content():
    prompt = request.json.get('prompt')
    api_key = request.json.get('apiKey')  # Ensure the API key is passed here if needed

    try:
        # Generate content using the Gemini model
        generated_content = content_generator(prompt, max_length=200, num_return_sequences=1)
        return jsonify({'content': generated_content[0]['generated_text']})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/moderate', methods=['POST'])
def moderate_content():
    content = request.json.get('content')
    api_key = request.json.get('apiKey')  # Ensure the API key is passed here if needed

    try:
        # Moderate content using the Gemini model
        moderation_result = content_moderator(content)
        return jsonify({'moderation_result': moderation_result[0]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
