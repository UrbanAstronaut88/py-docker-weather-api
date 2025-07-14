FROM python:3.12-slim

LABEL maintainer="bku089@gmail.com"

WORKDIR /app

COPY requirements.txt .

COPY app/ ./app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app/main.py"]
