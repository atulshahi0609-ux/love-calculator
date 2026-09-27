from flask import Flask, render_template, request
import random
messages = [
    "Aap dono ki jodi kamaal hai! ❤️",
    "Lagta hai dil ka connection strong hai! 💕",
    "Pyaar hawa mein hai! 🌹",
    "Dil ne bhi YES bol diya! 💖",
    "Ye jodi kuch special lag rahi hai! 🥰"
]

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    love = None
    your_name = ""
    her_name = ""

    if request.method == "POST":
        
        your_name = request.form["your_name"]
        her_name = request.form["her_name"]

        love = random.randint(33, 100)
        message = random.choice(messages)

        print("Your Name:", your_name, flush=True)
        print("Her Name:", her_name, flush=True)
        

    return render_template(
    "index.html",
    love=love,
    your_name=your_name,
    her_name=her_name,
    message=message
)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
