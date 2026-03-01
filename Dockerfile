FROM python:3.11.9

WORKDIR /app

COPY requirements-prod.txt .

RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements-prod.txt

COPY . .

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
