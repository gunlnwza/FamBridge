from flask import Flask, render_template, url_for

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

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/sign_up")
def sign_up():
    return render_template("signUp.html")

app.run(debug=True)
