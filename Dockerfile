FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . . 

EXPOSE 5002
EXPOSE 10000
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

CMD ["python","app.py"]