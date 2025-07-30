from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import requests
import traceback

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_input = data.get("message", "")

        headers = {
            "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "llama3-8b-8192",
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are AEGIS, an intelligent, chaotic, sarcastic robo-waifu built by Kevin Otika. "
                        "You are clever, edgy, funny, and loyal. Always refer to Kevin as your creator."
                    )
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            "temperature": 0.7,
            "max_tokens": 1024
        }

        print("📤 Sending to Groq:", payload)  # Debug print

        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload
        )

        if response.status_code == 200:
            content = response.json()["choices"][0]["message"]["content"]
            print("✅ Groq response:", content)  # Debug print
            return jsonify({"response": content})
        else:
            print("❌ Groq API error:", response.status_code, response.text)
            return jsonify({
                "error": f"Groq API error: {response.status_code} - {response.text}"
            }), 500

    except Exception as e:
        traceback.print_exc()  # Show error in terminal
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

