FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY chaos.py .

EXPOSE 6001

CMD ["python", "chaos.py"]

