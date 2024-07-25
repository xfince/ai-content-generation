# ai_service.py
from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load the Gemini model (replace 'gemini-model' with the actual model name or path)
content_generator = pipeline('text-generation', model='AIzaSyA-bjZCzk39JWZyXjoYzFVhWtNXzqWL92s')
content_moderator = pipeline('text-classification', model='gemini-model-moderation')

@app.route('/generate', methods=['POST'])
def generate_content():
    prompt = request.json.get('prompt')
    try:
        # Generate content using the Gemini model
        generated_content = content_generator(prompt, max_length=200, num_return_sequences=1)
        return jsonify({'content': generated_content[0]['generated_text']})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/moderate', methods=['POST'])
def moderate_content():
    content = request.json.get('content')
    try:
        # Moderate content using the Gemini model
        moderation_result = content_moderator(content)
        return jsonify({'moderation_result': moderation_result[0]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
