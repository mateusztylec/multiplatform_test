FROM python:3.11-alpine3.16

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

CMD ["uvicorn" ,"main:app", "--host", "0.0.0.0"]

EXPOSE 8000