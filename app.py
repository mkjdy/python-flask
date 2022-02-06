from flask import Flask, render_template, request, flash, url_for, redirect
from forms import SignUpForm
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config["SECRET KEY"] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///authors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(app)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), default="")

    def __init__(self, name, title, content):
        self.name = name
        self.title = title
        self.content = content

    def __repr__(self):
        return '<Author %r>' % self.id


db.create_all()
db.session.commit()

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


@app.route('/list', methods=['GET'])
def list_authors():
    authors = Author.query.all()
    return render_template('list_authors.html', authors=authors, title="Author's List")


@app.route('/add', methods=['GET', 'POST'])
def add_authors():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['title'] or not request.form['content']:
            flash('Please enter all the fields', 'error')
        else:
            author = Author(request.form['name'], request.form['title'], request.form['content'])

            db.session.add(author)
            db.session.commit()
            flash('Thanks for the awesome info')
            return redirect(url_for('list_authors'))
    return render_template('add_author.html')


if __name__ == '__main__':
    app.run(debug=True)

