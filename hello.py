from flask_moment import Moment
from flask_bootstrap import Bootstrap
from flask import render_template,session, redirect, url_for,flash
from flask import  Flask
from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import DataRequired
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:qwert12345@localhost:3306/apitest?charset=utf8mb4'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<User %r>' % self.username

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    password = PasswordField('What is your password?', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        session['password'] = form.password.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), password=session.get('password'))

if __name__=='__main__':
    app.run(debug=True)