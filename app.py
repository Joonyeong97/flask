from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("corona1911.html")


@app.route('/corona19')
def corona19():
    return render_template("corona19_0225.html")

@app.route('/corona19z')
def corona192():
    return render_template("corona19_20200226.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
