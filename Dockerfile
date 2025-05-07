FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . . 

EXPOSE 5002

ENV FLASK_APP=app.py
ENV FLASK_ENV=production

CMD ["python","app.py"]

#estava dando  erro no docker porque, inicialmente ele foi posto como DockerFile, mas mudou para dockerfile
# git mv DockerFile Dockerfile, renomeando de novo
# git status
# Changes to be committed:
#     (use "git restore --staged <file>..." to unstage)
#           deleted:    DockerFile
#           modified:   Dockerfile