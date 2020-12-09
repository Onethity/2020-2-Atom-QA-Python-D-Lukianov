""" Небольшое приложение на Flask для нагрузочного тестирования """

from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from application.config import APP_HOST, APP_PORT, APP_USERS

app = Flask(__name__)
auth = HTTPBasicAuth()

users = APP_USERS


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


@app.route('/')
@auth.login_required
def index():
    return f'Hello {auth.current_user()}!'


@app.route('/profile')
@auth.login_required
def profile():
    return f"{auth.current_user()}'s profile"


@app.route('/album')
@auth.login_required
def album():
    return f"{auth.current_user()}'s album"


@app.route('/photo')
@auth.login_required
def photo():
    return f"It's a photo of you, dear {auth.current_user()}!"


@app.route('/shareware')
def shareware():
    return 'Free for all!'


@app.route('/logout')
@auth.login_required
def logout():
    return f'Bye {auth.current_user()}!', 401


if __name__ == '__main__':
    app.run(debug=False, host=APP_HOST, port=APP_PORT)
