FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 50051 8000

CMD sh -c "python grpc_server.py & uvicorn api:app --host 0.0.0.0 --port 8000"
