from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route('/main')
def index():
    return render_template("main.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/corona')
def blog():
    return render_template("corona.html")

@app.route('/issue')
def issue():
    return render_template("issue.html")

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


@app.route('/twitter')
def twitter():
    return render_template("analysis/twitter.html")

@app.route('/naver')
def naver():
    return render_template("analysis/naver.html")

@app.route('/daum')
def daum():
    return render_template("analysis/daum.html")

@app.route('/map')
def map():
    return render_template("map1.html")

if __name__ == '__main__':
    start = input('온라인은 y / 오프라인은 아무키나 : ')
    if start == 'y':
        app.run(host='0.0.0.0', port=80)
    else:
        app.run(host='127.0.0.1', port=80)