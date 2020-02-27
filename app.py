from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route('/main')
def index():
    return render_template("main.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/blog')
def blog():
    return render_template("blog.html")

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/elements')
def elements():
    return render_template("elements.html")

@app.route('/')
def main1():
    return render_template("index.html")

@app.route('/index')
def index2():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)