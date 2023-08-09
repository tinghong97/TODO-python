FROM python:3.9.0

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip freeze > requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]