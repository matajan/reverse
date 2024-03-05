FROM python:3.9-alpine

WORKDIR /app

COPY reverse.py .

EXPOSE 8000

CMD [ "python3", "reverse.py" ]
