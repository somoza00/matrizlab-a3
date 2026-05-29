FROM python:3.10-slim

WORKDIR /app

COPY *.py ./

CMD ["python", "main.py"]
