from flask import Flask, render_template, request
from forms import SignUpForm
import os

app = Flask(__name__)
# app.config["SECRET KEY"] = "secret"

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

posts = [
    {
        "author" : "Barbara Go",
        "title" : "Jumpin Fun",
        "content" : "Lots of frog",
        "date_posted" : "April 3, 2021"
    },
    {
        "author" : "Jake Daza",
        "title" : "Grizzly Jaws",
        "content" : "The bite of grizzly bear",
        "date_posted" : "April 4, 2021"
    }
]

@app.route('/')
# same redirector
@app.route('/home')
def home():
    return render_template('home.html', title="Home Page Here")

@app.route('/animal')
def animal():
    return render_template('animal.html', posts=posts, title="Fun Animal Facts")

@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template("userdata.html", result=result)
    return render_template('signup.html', form=form, title="Sign Up Here")
