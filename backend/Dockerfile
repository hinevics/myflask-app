FROM python:3.8.3

RUN mkdir -p /src/
WORKDIR /src/

COPY . /src/
RUN pip install --no-cache-dir -r requirements.txt

ENV TZ Europe/Moscow

EXPOSE 8080
EXPOSE 27017

CMD ["python", "run.py"] 