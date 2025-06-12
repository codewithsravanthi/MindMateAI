from flask import Flask, render_template, request, jsonify
import random
import datetime

app = Flask(__name__)

quotes = [
    "You're stronger than you think 🌟",
    "Every day is a fresh start 🌿",
    "You're not alone, I'm here with you 💛",
    "Keep going, even small steps matter 🚶‍♀️",
    "You are worthy of love and healing 💖"
]

def greeting():
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "Good morning 🌞"
    elif 12 <= hour < 17:
        return "Good afternoon ☀️"
    else:
        return "Good evening 🌙"

def generate_response(user_input, name="friend"):
    user_input = user_input.lower()
    reply = ""

    if "sad" in user_input:
        reply = f"I'm sorry you're feeling sad, {name}. Want to talk about it?"
    elif "anxious" in user_input or "nervous" in user_input:
        reply = f"It's okay to feel anxious, {name}. Deep breaths. I'm here for you 🌬️"
    elif "happy" in user_input:
        reply = f"That's wonderful to hear, {name}! 😊 What made you happy today?"
    elif "angry" in user_input:
        reply = f"Anger is natural, {name}. Do you want to share what's causing it?"
    elif "confused" in user_input:
        reply = f"It’s okay to feel confused, {name}. Let’s figure it out together 🧩"
    elif "lonely" in user_input:
        reply = f"You’re not alone, {name}. I'm always here with you 🤗"
    elif "hello" in user_input or "hi" in user_input:
        reply = f"{greeting()}, {name}! I'm MindMate. How are you feeling today?"
    else:
        reply = f"I'm here to listen, {name}. Please tell me more about what you're feeling."

    reply += "\n\n💬 *" + random.choice(quotes) + "*"
    return jsonify({"reply": reply})

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    user_name = data.get("name", "friend")
    return generate_response(user_input, user_name)

if __name__ == "__main__":
    app.run(debug=False)
