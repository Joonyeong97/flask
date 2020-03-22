from flask import render_template, request, redirect, url_for
from flask import Flask, abort, flash
from werkzeug.utils import secure_filename
import titanic
import img_load
import sql
import os

app = Flask(__name__)

###### TEST #######
###### TEST #######
###### TEST #######
# file name : test.py
# pwd : /project_name/app/test/test.py
###### TEST #######
###### TEST #######
###### TEST #######

# 업로드 HTML 렌더링
@app.route('/catdog')
def render_file():
    return render_template('img_dir/img_upload.html')


# 파일 업로드 처리
@app.route('/catdog2', methods=['GET', 'POST'])
def upload_file():
    import os
    from flask import jsonify
    if request.method == 'POST':
        img_dir = os.path.join('static/customer_img/')
        f = request.files['file']
        # 저장할 경로 + 파일명
        f.save(img_dir+secure_filename(f.filename))
        dap = img_load.cat_dog(f.filename)
        name = img_load.panbyul(dap)
        return render_template('img_dir/img_load.html', dap=dap, name=name)
    return render_template('img_dir/img_load.html')



# IP 주소확인
@app.route('/ip', methods=['GET'])
def name():
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    print('현재 접속한 ip : ',ip)
    return request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    #return jsonify({'ip': request.remote_addr}), 200
    #return jsonify({'ip': request.environ['REMOTE_ADDR']}), 200
# 문의글
@app.route('/pop')
def pop():
	return render_template('Testing/popup.html')

@app.route('/ok', methods=['POST'])
def ok_():
    if request.method == 'POST':
        nick = request.form['nick']
        text = request.form['text']
        email = request.form['email']
        ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        if len(nick) == 0 or len(text) == 0 or len(email) == 0:
            return render_template('Testing/error.html')
        else:
            sql.inquire(nick, email, text, ip)
            return render_template('Testing/ok_.html', nick=nick, text=text, email=email)
# 문의글 끝

# 타이타닉 시작
@app.route('/titanic1')
def titanic1():
	return render_template('Testing/titanic1.html')


# 타이타닉 결과물
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


@app.route('/deepleaning')
def deepleaning():
    return render_template("deepleaning.html")


@app.route('/machineleaning')
def machineleaning():
    return render_template("machineleaning.html")

@app.route('/test')
def test_():
	return render_template('Testing/test.html')

@app.route('/base')
def index():
    try:
        today = sql.today()
    except:
        abort(404, description="Resource not found")
    return render_template("base.html", today=today)

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


@app.route('/', methods=['GET'])
def main1():
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    sql.connection_ip(ip)
    try:
        today = sql.today()
        total = sql.total()
    except:
        abort(404, description="Resource not found")
    return render_template("index.html", today=today, total=total)

@app.route('/index', methods=['GET'])
def index2():
    try:
        today = sql.today()
        total = sql.total()
    except:
        abort(404, description="Resource not found")
    return render_template("index.html", today=today, total=total)

@app.route('/twitter02')
def twitter02():
    return render_template("analysis/twitter/twitter02.html")
@app.route('/twitter03')
def twitter03():
    return render_template("analysis/twitter/twitter03.html")



@app.route('/naver02')
def naver02():
    return render_template("analysis/naver/naver02.html")
@app.route('/naver03')
def naver03():
    return render_template("analysis/naver/naver03.html")



@app.route('/daum02')
def daum02():
    return render_template("analysis/daum/daum02.html")
@app.route('/daum03')
def daum03():
    return render_template("analysis/daum/daum03.html")


if __name__ == '__main__':
    start = input('온라인은 y / 오프라인은 아무키나 : ')
    if start == 'y':
        app.run(host='0.0.0.0', port=80)
    else:
        app.run(host='127.0.0.1', port=80)