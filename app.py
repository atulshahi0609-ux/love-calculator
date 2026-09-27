from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    love = None
    your_name = ""
    her_name = ""
    message = ""

    if request.method == "POST":

        your_name = request.form["your_name"]
        her_name = request.form["her_name"]

        # Random Love Percentage
        love = random.randint(1, 100)

        # Love Percentage ke hisaab se message
        if love <= 30:
            message = "Thoda aur effort karo! 😄❤️"

        elif love <= 60:
            message = "Cute connection hai! 💕"

        elif love <= 80:
            message = "Pyaar ka connection strong hai! ❤️"

        elif love < 100:
            message = "Wah! Ye toh serious love hai! 🔥❤️"

        else:
            message = "TRUE LOVE! 💖🌹"

        # Render logs me names dikhane ke liye
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
