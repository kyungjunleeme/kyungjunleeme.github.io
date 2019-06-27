import os
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from models import db

from models import Fcuser

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        userid = request.form.get('userid')
        username = request.form.get('username')
        password = request.form.get('password')
        re_password = request.form.get('re-password')

        if (userid and username and password and re_password) and password == re_password:
            fcuser = Fcuser()
            fcuser.userid = userid
            fcuser.username = username
            fcuser.password = password

            db.session.add(fcuser)
            db.session.commit()

            return redirect('/')

    return render_template('register.html')

@app.route('/')
def hello():
    return render_template('hello.html')

if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__))
    dbfile = os.path.join(basedir, 'db.sqlite')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    db.app = app
    db.create_all()
    app.run(host='127.0.0.1', port=5000, debug=True)


pip install Flask-WTF

html

python form 을 만들어서 tmeplate 전달해서

csrf 보호 기법 
사이트 간 요청 위조


form 
from flaks_wtf.csrf import CSRFProtect
from forms import RegisterForm



app.config['SECRET_KEY'] = 'qwerqwerqwerqwerqwer'

csrf = CSRFProtect()
csrf.init_app(app)


from flaks_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    userid = StringField('userid', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # login!
        return redirect('/')
    return render_template('login.html', form=form)

# login.html

세션이란
쿠키 정보 없이 요청이 오면 

다음 요청 때는 쿠키를 같이 요청함. 
쿠키 원하는 
세션은 클라이언트와 서버간의 정보를 유지하기 위해 사용됨

세션에 어떤 데이터를 저장해야하는지 
세션이라는 변수 안에 값만 저장해주면, client가 분류되고, session 정보도 각 client 마다 사용 가능함
session['userid'] = form.data.get('userid')

userid = session.get('userid', None)

{% if userid %}
{{userid}}
{% endif %}

class LoginForm(FlaskForm):
    class UserPassword(object):
        def __init__(self, message=None):
            self.message = message
    
    def __call__(self, form, field):
        userid = form.['userid'].data
        password = field.data

        fcuser = Fcuser.query.filter_by(userid=userid).first()
        if fcuser.password != password:
            raise ValueError('Wrong password')
    

    userid = StringField('userid', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), UserPassword()])

    {{ form.password.label("q")}}

    
@app.route('/logout', methods=['GET'])
def logout():
    session.pop('userid', None)
    return redirect('/')



<a href="/logout">로그아웃



































