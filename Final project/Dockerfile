# Докер файл для создания образа с тестами
# Для использования нужно примонтировать тесты в папку /tests и запустить pytest

FROM python:3.8.6

WORKDIR /tests

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

