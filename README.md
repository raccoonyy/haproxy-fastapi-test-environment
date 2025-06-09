# HAProxy 테스트 환경

### 테스트 서버 실행 (HAProxy + FastAPI)
```shell
docker compose up
```

### 테스트 스크립트

```shell
./test.sh
```

혹은

```shell
curl -X PUT http://localhost:8080/kontrol/test \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer first-test-token" \
  -d '{"message": "test message"}'
```