FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . . 

EXPOSE 5002

CMD ["python","apps/app.py"]