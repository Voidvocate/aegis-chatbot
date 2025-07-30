AEGIS (Groq Edition) - Chatbot Backend + Client
===============================================

1. Install dependencies:
   pip install -r requirements.txt

2. Rename `.env.example` to `.env` and paste your Groq API key.

3. Open `server.py` and replace YOUR_GROQ_API_KEY with your key if not using .env.

4. Start the Flask server:
   python server.py

5. In another terminal, run the chatbot client:
   python aegis_client.py

This version uses the Mixtral model via Groq — super fast and free.
