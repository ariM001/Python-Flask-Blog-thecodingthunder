from flask import Flask, flash, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail    # pip install flask-mail
import json
from datetime import datetime
import os
from werkzeug.utils import secure_filename


with open('config.json', 'r') as c:
    params = json.load(c)['params']

app = Flask(__name__)
app.secret_key = 'super-sectet-key'
app.config['UPLOAD_FOLDER'] = params['upload_location']

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
        return render_template('dashboard.html', params=params, posts=posts)

    if request.method == "POST":
        username = request.form.get('uname')
        password = request.form.get('pass')

        if (username == params['admin_username'] and password == params['admin_password']):
            # set the session variable
            session['user'] = username
            posts = Posts.query.all()
            return render_template('dashboard.html', params=params, posts=posts)

        else:
            flash('Invalid Credentials!', 'warning')
            return redirect('/dashboard')

    return render_template('login.html', params=params)


@app.route('/logout')
def logout():
    session.pop('user')
    flash('You have successfully logged out', 'info')
    return redirect('/dashboard')


@app.route("/edit/<string:sno>", methods=['GET', 'POST'])
def edit(sno):
    # if the user is already logged in
    if ('user' in session and session['user'] == params['admin_username']):
        if request.method == "POST":
            box_title = request.form.get('title')
            box_slug = request.form.get('slug')
            box_tagline = request.form.get('tagline')
            box_author = request.form.get('author')
            box_content = request.form.get('content')
            box_image = request.form.get('image')

            if sno == '0':  # adding a new post
                post = Posts(title=box_title, slug=box_slug, tagline=box_tagline,
                             author=box_author, content=box_content, img_file=box_image, date=datetime.now())
                db.session.add(post)
                db.session.commit()
                flash('Post Added Successfully!', 'info')
                return redirect('/dashboard')

            else:   # editing an existing post
                post = Posts.query.filter_by(sno=sno).first()
                post.title = box_title
                post.slug = box_slug
                post.tagline = box_tagline
                post.author = box_author
                post.content = box_content
                post.img_file = box_image
                post.date = datetime.now()
                db.session.commit()
                flash('Changes Saved Successfully!', 'info')
                return redirect('/edit/'+sno)

        post = Posts.query.filter_by(sno=sno).first()
        return render_template('edit.html', params=params, post=post, sno=sno)

    # if the user is not logged in
    else:
        flash('You must login to continue', 'warning')
        return redirect('/dashboard')



@app.route("/uploader", methods=['GET', 'POST'])
def uploader():
    if ('user' in session and session['user'] == params['admin_username']):
        if request.method == "POST":
            f = request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
            flash('File Uploaded Successfully!', 'info')
            return redirect('/dashboard')


@app.route("/delete/<string:sno>", methods=['GET', 'POST'])
def delete(sno):
    if ('user' in session and session['user'] == params['admin_username']):
        if request.method == "POST":
            confirmpass = request.form.get('confirmpass')
            if confirmpass == params['admin_password']:
                post_del = Posts.query.filter_by(sno=sno).first()
                db.session.delete(post_del)
                db.session.commit()
                flash('Post deleted successfully', 'warning')
                return redirect('/dashboard')


app.run(debug=True)
