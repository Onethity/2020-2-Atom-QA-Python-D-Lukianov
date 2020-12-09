from werkzeug.security import generate_password_hash

APP_HOST = '0.0.0.0'
APP_PORT = 4215

# Список пользователей для авторизации
APP_USERS = {
    'Dima': generate_password_hash('123'),
    'Max': generate_password_hash('321'),
}
