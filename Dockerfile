FROM python:3.10-slim

WORKDIR /app

# Устанавливаем wait-for-it и необходимые зависимости для psycopg2-binary
RUN apt-get update && apt-get install -y \
    wait-for-it \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
ENV PYTHONPATH=/app

CMD ["wait-for-it", "db:5432", "--timeout=60", "--", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
