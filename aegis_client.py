import requests

print("🔮 AEGIS is online. Type 'exit' to shut her down.")

while True:
    msg = input("You: ")
    if msg.lower() in ["exit", "quit"]:
        break

    try:
        res = requests.post("http://127.0.0.1:5000/chat", json={"message": msg})
        print("AEGIS:", res.json().get("response", "Error: no response"))
    except Exception as e:
        print("❌ Connection error:", e)

