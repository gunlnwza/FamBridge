from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/aboutUs")
def aboutUs():
    return render_template("aboutUs.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.route("/finding")
def finding():
    return render_template("finding.html")

app.run(debug=True)
