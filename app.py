from flask import render_template, request, redirect, url_for
from flask import Flask, abort, flash
import titanic
import sql

app = Flask(__name__)

###### TEST #######
###### TEST #######
###### TEST #######
# file name : test.py
# pwd : /project_name/app/test/test.py
###### TEST #######
###### TEST #######
###### TEST #######
@app.route('/ip', methods=['GET'])
def name():
    return request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    #return jsonify({'ip': request.remote_addr}), 200
    #return jsonify({'ip': request.environ['REMOTE_ADDR']}), 200


#Define a route for url
@app.route('/titanic1')
def titanic1():
	return render_template('Testing/titanic1.html')


#form action
@app.route('/titanic2', methods=['POST'])
def titanic2():
    try:
        if request.method == 'POST':
            pclass = request.form['pclass']
            sex = request.form['sex']
            age = request.form['age']
            Fare = request.form['Fare']
            embarked = request.form['embarked']
            name = request.form['name']
            isalone = request.form['isalone']
            if len(pclass) == 0 or len(sex) == 0 or len(age) == 0 or len(Fare) == 0 or len(embarked) == 0 or len(name) == 0 or len(isalone) == 0:
                #flash('You were successfully logged in')
                return render_template('Testing/error.html')
            else:
                pa = titanic.titanic_m(pclass, sex, age, Fare, embarked, name, isalone)
                return render_template('Testing/titanic2.html', pclass=pclass, sex=sex, age=age, Fare=Fare, embarked=embarked, name=name, isalone=isalone, pa=pa)
    except:
        abort(404, description="Resource not found")
    return render_template('Testing/titanic2.html')



@app.route('/machineleaning')
def machineleaning():
    return render_template("machineleaning.html")




@app.route('/test')
def test_():
	return render_template('Testing/test.html')

@app.route('/base')
def index():
    return render_template("base.html")

@app.route('/error')
def error_m(error):
    return render_template('Testing/error.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('Testing/404.html')


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