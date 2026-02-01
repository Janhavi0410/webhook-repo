from flask import Flask, request

app = Flask(__name__)

# Home route to check if server is running
@app.route("/")
def home():
    return {"message": "TechStaX server running"}

# Webhook endpoint to receive external events
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Received data:", data)  # log incoming webhook data
    return {"status": "Webhook received"}

if __name__ == "__main__":
    app.run(debug=True)

