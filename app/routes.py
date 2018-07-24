from app import app
from flask import render_template


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