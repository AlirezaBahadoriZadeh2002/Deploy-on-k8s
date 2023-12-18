FROM python:3.10.0-alpine3.15

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src src

EXPOSE 5000

ENTRYPOINT ["python", "./src/app.py"]
