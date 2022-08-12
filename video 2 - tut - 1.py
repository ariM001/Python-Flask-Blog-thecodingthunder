from flask import Flask

app = Flask(__name__)

@app.route("/")    # this is one end point
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/harry")        # this is another end point
def hello_harry():
    return "<p>Hello Harry, Good Afternoon!</p>"

app.run(debug=True)