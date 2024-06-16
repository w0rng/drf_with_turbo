FROM python:3.12-alpine

WORKDIR /app

COPY entrypoint.sh .

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir && \
    chmod +x entrypoint.sh .


COPY src/ .
ENTRYPOINT ["/app/entrypoint.sh"]