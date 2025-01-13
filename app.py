from flask import Flask, request, render_template, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = "top_secret_secret_key"

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
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        if not (email and password):
            return render_template("signUp.html", message="All fields are required.")

        hashed_password = generate_password_hash(password)

        try:
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                           (username, email, hashed_password))
            conn.commit()
            conn.close()
        except sqlite3.IntegrityError:
            return render_template("signUp.html", message="Username or Email already exists.")

        return redirect("/login")

    return render_template("signUp.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        # retrieve user
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, username, email, password FROM users WHERE email = ?', (email,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[3], password):
            session["user_id"] = user[0]
            print(user[0], user[1], "login successfully")
            return redirect("/user_home")
        else:
            return render_template("login.html", message="Invalid username or password.")

    return render_template("login.html")

@app.route("/user_home")
def user_home():
    if 'user_id' not in session:
        return redirect('/')
    user_id = session['user_id']

    return render_template("user_home.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

app.run(debug=True)
