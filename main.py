from flask import Flask, flash, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail    # pip install flask-mail
import json
from datetime import datetime


with open('config.json', 'r') as c:
    params = json.load(c)['params']

app = Flask(__name__)
app.secret_key = 'super-sectet-key'

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
    slug = db.Column(db.String(),  nullable=False)
    title = db.Column(db.String(), nullable=False)
    tagline = db.Column(db.String(), nullable=False)
    author = db.Column(db.String(), nullable=False)
    content = db.Column(db.String(),  nullable=False)
    img_file = db.Column(db.String(), nullable=True)
    date = db.Column(db.String(12), nullable=True)


class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(25),  nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    mes = db.Column(db.String(150),  nullable=False)
    date = db.Column(db.String(12), nullable=True)


@app.route("/")
def home():
    all_post = Posts.query.filter_by().all()[0:params['no_of_posts']]
    return render_template('index.html', params=params, all_post=all_post)


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

        if len(name) < 3 or len(name) > 20:
            flash('Name is too short or too lengthy!', 'warning')
            return redirect('/contact')
        if len(email) < 6 or len(email) > 25:
            flash('Email is too short or too lengthy!', 'warning')
            return redirect('/contact')
        if len(phone_num) < 10 or len(phone_num) > 15:
            flash('Phone number is too short or too lengthy!', 'warning')
            return redirect('/contact')
        if len(mes) < 8 or len(mes) > 100:
            flash('Message is too short or too lengthy!', 'warning')
            return redirect('/contact')

        entry = Contacts(name=name, email=email,
                         phone_num=phone_num, mes=mes, date=datetime.now())

        db.session.add(entry)
        db.session.commit()
        flash('Your message has been sent successfully!', 'info')

        # mail.send_message('TheCodingThunder: New message from ' + name,
        #                   sender=email,
        #                   recipients=[params['gmail_user']],
        #                   body=mes,)

        return redirect('/contact')

    return render_template('contact.html', params=params)


@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    if ('user' in session and session['user'] == params['admin_username']):
        # give access to admin page because user is already logged in
        posts = Posts.query.all()
        return render_template('dashboard.html', params=params, posts = posts)
 

    if request.method == "POST":
        username = request.form.get('uname')
        password = request.form.get('pass')
        
        if (username == params['admin_username'] and password == params['admin_password']):
            # set the session variable
            session['user'] = username
            posts = Posts.query.all()
            return render_template('dashboard.html', params=params, posts = posts)
        
        else:
            flash('Invalid Credentials!', 'warning')
            return redirect('/dashboard')

    return render_template('login.html', params=params)

app.run(debug=True)
