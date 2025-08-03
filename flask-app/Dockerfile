FROM python:3.9-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install prometheus-flask-exporter

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]

