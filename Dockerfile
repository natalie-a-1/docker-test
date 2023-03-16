FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip3 install flask

EXPOSE 3000

CMD python3 ./app.py
