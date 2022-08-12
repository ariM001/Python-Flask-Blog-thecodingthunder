from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")    # this is one end point
def index():
    return render_template('index.html')


@app.route("/about")        # this is another end point
def about():
    name = "Harry"
    return render_template('about.html',NAME = name)

app.run(debug=True)