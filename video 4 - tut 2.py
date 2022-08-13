from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")    # this is one end point
def index():
    return render_template('demo-index.html')


@app.route("/about")        # this is another end point
def about():
    name = "Harry"
    return render_template('demo-about.html',NAME = name)

@app.route("/bootstrap")
def bootstrap():
    return render_template('demo-bootstrap.html')

if __name__ == "__main__":
    app.run(debug=True)