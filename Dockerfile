# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copiar requirements y luego instalar
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

# Copiar la app
COPY . /app

# Exponer puerto
EXPOSE 5000

# Comando por defecto (gunicorn)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--workers", "1", "--threads", "4"]