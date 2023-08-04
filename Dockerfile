FROM python:3.8

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir Django

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
