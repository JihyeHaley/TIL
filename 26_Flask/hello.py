from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_word():
    return 'Hello, World!'


@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/jihye')
def jihye():
    return 'Jihye'


'''
default is string
'''
from  markupsafe import escape
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_idx):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_idx

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /patht/
    return 'Subpath %s' % escape(subpath)

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'


'''
url_for
'''
from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)
# @app.route('/')
# def index():
#     return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<str:username>')
def profile(username):
    return '{}\'s profile' .format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='Haley Oh'))