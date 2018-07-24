from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kelvin'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Nairobi!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Movie was cool'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for {}, remeber_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='sign in', form=form)
