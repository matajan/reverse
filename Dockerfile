FROM python:3.9-alpine

COPY reverse.py /app

WORKDIR /app

EXPOSE 8000

CMD [ "python3", "reverse.py" ]
