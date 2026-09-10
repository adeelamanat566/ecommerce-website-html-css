FROM python:3.14 AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt





FROM python:3.14-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .
CMD ["python","app.py"]