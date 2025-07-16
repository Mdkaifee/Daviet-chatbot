from flask import Flask, request, jsonify, render_template
from chatbot.bot import get_bot_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    # Render your chat UI page
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    response = get_bot_response(user_message)
    return jsonify({"response": response})

# Optional: If you want /chat to also serve the chat UI for GET requests
@app.route("/chat", methods=["GET"])
def chat_page():
    return render_template("chat.html")

if __name__ == "__main__":
    app.run(debug=True)
