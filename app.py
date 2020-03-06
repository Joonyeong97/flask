from flask import render_template, request, redirect, url_for
from flask import Flask

app = Flask(__name__)
###### TEST #######
###### TEST #######
###### TEST #######


#Define a route for url
@app.route('/login')
def form():
	return render_template('Testing/test.html')

#form action
@app.route('/hello', methods=['POST'] )
def action():
	firstname = request.form['firstname']
	lastname = request.form['lastname']
	email = request.form['email']
	return render_template('Testing/form_action.html', firstname=firstname, lastname=lastname, email=email)

@app.route('/base')
def index():
    return render_template("Testing/base.html")

###### TEST #######
###### TEST #######
###### TEST #######


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/corona02')
def corona02():
    return render_template("analysis/corona/corona02.html")
@app.route('/corona03')
def corona03():
    return render_template("analysis/corona/corona03.html")


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

@app.route('/corona')
def corona_home():
    return render_template("corona_home.html")

if __name__ == '__main__':
    start = input('온라인은 y / 오프라인은 아무키나 : ')
    if start == 'y':
        app.run(host='0.0.0.0', port=80)
    else:
        app.run(host='127.0.0.1', port=80)