"""
Мок VK ID API на flask
"""

import threading

from flask import Flask, request, jsonify

from mock.config import MOCK_CONFIG

app = Flask(__name__)

DATA = {'dima': '123'}  # Переменная для хранения БД мока


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
    """ Эндпоинт для остановки мока """
    stop_app()


@app.route('/vk_id/<username>')
def check_username(username):
    """ Получение VK ID пользователя username """
    if username in DATA:
        return jsonify({'vk_id': DATA.get(username)})
    else:
        return jsonify({}), 404


@app.route('/vk_id/add_user', methods=['POST'])
def add_user():
    """ Добавление VK ID в базу"""
    request_data = request.get_json()
    DATA.update({
        request_data['username']: request_data['vk_id']
    })

    return jsonify({'status': 'ok'})


@app.route('/is_mock_up')
def is_mock_up():
    """ Роут для проверки, что мок поднят """
    return 'OK'


if __name__ == '__main__':
    start_app(MOCK_CONFIG['host'], MOCK_CONFIG['port'])
