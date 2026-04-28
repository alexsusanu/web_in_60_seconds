# app.py
from flask import Flask, request

app = Flask(__name__)

@app.post("/webhook")
def webhook():
    data = request.json
    print("RECEIVED:", data)
    return "", 200

if __name__ == "__main__":
    app.run(port=8000)
