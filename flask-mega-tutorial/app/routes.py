from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'lime'}
    posts = [
        {
            'author': {'username': 'berry'},
            'body': 'Strawberry Fields Forever'
        },
        {
            'author': {'username': 'summer'},
            'body': 'Summertime Sadness'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)