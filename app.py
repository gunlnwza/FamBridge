from flask import Flask, request, render_template, redirect, session, url_for
from werkzeug.security import generate_password_hash

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about_us")
def about_us():
    return render_template("aboutUs.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.route("/finding")
def finding():
    return render_template("finding.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if not (email and password):
            return render_template("signUp.html", message="All fields are required.")

        hashed_password = generate_password_hash(password)

        # store user data in db
        # TODO: db insertion code here
        print("insert", email, hashed_password)

        return redirect("/login")

    return render_template("signUp.html")

@app.route("/login")
def login():
    return render_template("login.html")

app.run(debug=True)
