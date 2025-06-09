FROM python:3.13

WORKDIR /app

RUN pip install uv
COPY . .
RUN uv sync

# 인증서 디렉토리 생성
RUN mkdir -p /app/certs

# 인증서 복사
COPY certs/cert.pem /app/certs/
COPY certs/key.pem /app/certs/

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0", "--port", "8000", "--ssl-keyfile", "/app/certs/key.pem", "--ssl-certfile", "/app/certs/cert.pem", "--log-level", "trace"]