from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime


with open('config.json', 'r') as c:
    params = json.load(c)['params']

app = Flask(__name__)

local_server = params['local_server']

if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)


class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(25),  nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    mes = db.Column(db.String(150),  nullable=False)
    date = db.Column(db.String(12), nullable=True)


@app.route("/")
def home():
    return render_template('index.html', params=params)


@app.route("/about")
def about():
    return render_template('about.html', params=params)


@app.route("/post")
def post():
    return render_template('post.html', params=params)


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
        return redirect('/')

    return render_template('contact.html', params=params)


app.run(debug=True)
