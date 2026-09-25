from flask import Flask, render_template, request
import random

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

        print("Your Name:", your_name)
        print("Her Name:", her_name)

    return render_template(
        "index.html",
        love=love,
        your_name=your_name,
        her_name=her_name
    )

app.run()
