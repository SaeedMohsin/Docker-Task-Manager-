FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

EXPOSE 5000

CMD ["sh", "-c", "python -c 'from app.database import init_db; init_db()' && gunicorn --bind 0.0.0.0:5000 --workers 2 app.app:app"]
