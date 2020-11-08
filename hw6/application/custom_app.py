"""
Основное приложение на Flask. Служит для управления списком пользователей.

Возможности:
    Отображение пользователей
    Добавление пользователей
    Удаление пользователей

Все запросы идут на '/' мока, вся логика там.

"""

import threading
import urllib.parse

import requests
from flask import Flask, request, jsonify

from config import CONFIG, MOCK_FULL_URL

app = Flask(__name__)


def start_app(host, port):
    server = threading.Thread(target=app.run, kwargs={
        'host': host,
        'port': port,
    })

    server.start()
    return server


def stop_app():
    stop_func = request.environ.get('werkzeug.server.shutdown')
    if stop_func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    else:
        stop_func()


@app.route('/stop')
def stop():
    """ Эндпоинт для остановки приложения """
    stop_app()


@app.route('/users')
def users_list():
    """ Отображение списка пользователей """
    try:
        mock_response = requests.get(MOCK_FULL_URL)  # Запрос на мок
    except requests.exceptions.ConnectionError:
        return jsonify({'status': 'error', 'message': 'users service not available'}), 421

    if mock_response.status_code == 200:
        # Если мок вернул 200, то отображаем список пользователей
        return mock_response.json()
    elif mock_response.status_code == 500:
        # Если мок вернул 500, то основное приложение возвращает код 424 Failed Dependency
        return jsonify({'status': 'error', 'message': 'users service internal error'}), 424
    else:
        return jsonify({'status': 'error', 'message': 'unknown error'}), mock_response.status_code


@app.route('/user/create', methods=['POST'])
def create_user():
    """ Создание нового пользователя """
    username = request.form['username']
    try:
        mock_response = requests.post(MOCK_FULL_URL, data=username)
    except requests.exceptions.ConnectionError:
        return jsonify({'status': 'error', 'message': 'users service not available'}), 421

    if mock_response.status_code == 200:
        return jsonify({'status': 'ok'})
    elif mock_response.status_code == 500:
        return jsonify({'status': 'error', 'message': 'users service internal error'}), 424
    else:
        return jsonify({'status': 'error', 'message': 'unknown error'}), mock_response.status_code


@app.route('/user/<username>', methods=['DELETE'])
def delete_user(username):
    try:
        mock_response = requests.delete(MOCK_FULL_URL, data=username)
    except requests.exceptions.ConnectionError:
        return jsonify({'status': 'error', 'message': 'users service not available'}), 421

    if mock_response.status_code == 200:
        return jsonify({'status': 'ok'})
    elif mock_response.status_code == 500:
        return jsonify({'status': 'error', 'message': 'users service internal error'}), 424
    elif mock_response.status_code == 400:
        return jsonify({'status': 'error', 'message': 'user does not exist'}), 400
    else:
        return jsonify({'status': 'error', 'message': 'unknown error'}), mock_response.status_code


@app.route('/timeout')
def timeout():
    """ Запрос на мок, где искусственно выставлен timeout """
    try:
        requests.get(urllib.parse.urljoin(MOCK_FULL_URL, '/timeout'), timeout=1)
        return jsonify({'status': 'no timeout'}), 200
    except requests.exceptions.ReadTimeout:
        return jsonify({'status': 'error', 'message': 'users service timeout'}), 408


@app.route('/mock_is_down')
def wrong_mock():
    """ Запрос на мок, который не запущен (не существует) """
    try:
        requests.get('http://172.16.123.256/')  # Такого ip не существует
        return jsonify({'status': 'ok'})
    except requests.exceptions.ConnectionError:
        return jsonify({'status': 'error', 'message': 'mock is down'}), 421


@app.route('/mock_500')
def mock_500():
    mock_response = requests.get(urllib.parse.urljoin(MOCK_FULL_URL, '/500'))

    if mock_response.status_code == 500:
        return jsonify({'status': 'error', 'message': 'mock service internal error'}), 424
    else:
        return jsonify({'status': 'error', 'message': 'unknown error'}), mock_response.status_code


@app.route('/check_auth/<username>', methods=['POST'])
def check_auth(username):
    """
     Проверка авторизации. Авторизация возможна, если данный пользователь
     существует в списке пользователей
    """
    if request.headers.get('Authorization'):
        # Если в приложение пришел хедер с авторизацией
        headers = {
            'Authorization': request.headers.get('Authorization')  # Передаем хедер из приложения в мок
        }
    else:
        headers = {}  # Иначе ничего не передаем

    mock_response = requests.post(
        urllib.parse.urljoin(MOCK_FULL_URL, '/auth'),
        headers=headers,
        data=username
    )

    if mock_response.status_code == 200:
        return jsonify({'status': 'ok'})
    elif mock_response.status_code == 412:
        return jsonify({'status': 'error', 'message': 'No auth header'}), mock_response.status_code
    elif mock_response.status_code == 403:
        return jsonify({'status': 'error', 'message': 'User does not exist'}), mock_response.status_code
    elif mock_response.status_code == 400:
        return jsonify({'status': 'error', 'message': 'Username in url and in header must be the same'}), mock_response.status_code
    else:
        return jsonify({'status': 'error', 'message': 'unknown error'}), mock_response.status_code


if __name__ == '__main__':
    start_app(CONFIG['app']['host'], CONFIG['app']['port'])
