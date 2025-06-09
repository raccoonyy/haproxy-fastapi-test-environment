from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json
import logging
from pythonjsonlogger import jsonlogger
import datetime

# JSON 로거 설정
logger = logging.getLogger()
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter(
    '%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

app = FastAPI()

@app.put("/test")
async def handle_put_request(request: Request):
    # 요청 헤더 수집
    headers = dict(request.headers)
    
    # 요청 바디 수집
    body = await request.body()
    try:
        body_json = json.loads(body)
    except:
        body_json = body.decode() if body else None
    
    # 로그 데이터 구성
    log_data = {
        "timestamp": datetime.datetime.now().isoformat(),
        "method": request.method,
        "headers": headers,
        "body": body_json,
        "client_host": request.client.host if request.client else None
    }
    
    # JSON 형식으로 로깅
    logger.info("Received PUT request", extra=log_data)
    
    return JSONResponse(
        content={
            "status": "success",
            "message": "Request logged successfully",
            "received_data": log_data
        }
    )
