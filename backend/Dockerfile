FROM python:3.8.3
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt
ADD . /app/