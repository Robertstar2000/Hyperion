from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os
import asyncio
from flask_cors import CORS # Import CORS

from gemini_client import generate_text_async, gemini_model

load_dotenv()

app = Flask(__name__)

# Enable CORS for all routes and all origins.
# For production, you should restrict origins to your frontend's domain.
CORS(app)
# Example for specific origins:
# CORS(app, resources={r"/api/*": {"origins": ["http://localhost:8000", "file://"]}})

# Test route
@app.route('/')
def home():
    return "Hello from Project Hypatia Backend! CORS is enabled."

@app.route('/api/generate', methods=['POST'])
def generate_endpoint():
    if not gemini_model:
        app.logger.error("Gemini API client not configured. Check API key and backend startup logs.")
        return jsonify({"error": "AI service is not configured on the server."}), 500

    data = request.get_json()
    if not data or 'prompt' not in data:
        app.logger.warning("Request received without prompt or invalid format.")
        return jsonify({"error": "Invalid request: No prompt provided or incorrect format."}), 400

    prompt = data['prompt']
    app.logger.info(f"Received prompt for /api/generate: '{prompt[:100]}...'") # Log received prompt (truncated)

    try:
        response_text = asyncio.run(generate_text_async(prompt))

        if response_text.startswith("Error:"):
            app.logger.error(f"Error from gemini_client: {response_text}")
            return jsonify({"error": response_text}), 500 # Internal server error from AI client side

        app.logger.info(f"Successfully generated text for prompt: '{prompt[:100]}...'")
        return jsonify({"text": response_text})

    except Exception as e:
        app.logger.error(f"Unexpected error in /api/generate: {e}", exc_info=True) # Log full exception info
        return jsonify({"error": f"An unexpected server error occurred."}), 500

if __name__ == '__main__':
    if not os.getenv("GEMINI_API_KEY"):
        print("CRITICAL: GEMINI_API_KEY is not set. The AI features will not work.")
        print("Please set it in the .env file or your environment.")

    # Added host='0.0.0.0' to make the server accessible from other devices on the network,
    # which can be useful for testing from a separate frontend dev environment if not using file://
    app.run(host='0.0.0.0', port=5000, debug=True)
