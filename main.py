from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail    # pip install flask-mail
import json
from datetime import datetime


with open('config.json', 'r') as c:
    params = json.load(c)['params']

app = Flask(__name__)

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['gmail_user'],
    MAIL_PASSWORD=params['gmail_password']
)
mail = Mail(app)

local_server = params['local_server']

if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)


class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(100),  nullable=False)
    title = db.Column(db.String(), nullable=False)
    author = db.Column(db.String(), nullable=False)
    content = db.Column(db.String(),  nullable=False)
    date = db.Column(db.String(12), nullable=True)
    img_file = db.Column(db.String(25), nullable=True)


class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(25),  nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    mes = db.Column(db.String(150),  nullable=False)
    date = db.Column(db.String(12), nullable=True)


@app.route("/")
def home():
    all_posts = Posts.query.all()
    return render_template('index.html', params=params, all_posts=all_posts)


@app.route("/about")
def about():
    return render_template('about.html', params=params)


@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params, post=post)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        # Add entry to the database
        name = request.form.get('name')
        email = request.form.get('email')
        phone_num = request.form.get('phone_num')
        mes = request.form.get('mes')

        entry = Contacts(name=name, email=email,
                         phone_num=phone_num, mes=mes, date=datetime.now())

        db.session.add(entry)
        db.session.commit()

        # mail.send_message('TheCodingThunder: New message from ' + name,
        #                   sender=email,
        #                   recipients=[params['gmail_user']],
        #                   body=mes,)

        return redirect('/')

    return render_template('contact.html', params=params)


app.run(debug=True)
