import os
import openai
<<<<<<< HEAD
from flask import Flask, request, jsonify

app = Flask(__name__)

# Use environment variable for OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/")
def home():
    return "✅ MindMate AI is running!"
=======
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")
>>>>>>> caf4d4a (✨ Added beautiful UI and frontend design)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
<<<<<<< HEAD

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

=======
>>>>>>> caf4d4a (✨ Added beautiful UI and frontend design)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are MindMate AI, a friendly mental wellness assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response['choices'][0]['message']['content']
        return jsonify({"reply": reply})
    except Exception as e:
<<<<<<< HEAD
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
=======
        return jsonify({"reply": "Oops! Something went wrong."})

if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> caf4d4a (✨ Added beautiful UI and frontend design)
