FROM python:3.8.6

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH="$PYTHONPATH:/app"

COPY . mock

ENTRYPOINT ["python", "mock/vk_id_mock.py"]

EXPOSE 4516