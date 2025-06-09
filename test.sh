curl -X PUT http://localhost:8080/custom/test \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer first-test-token" \
  -d '{"message": "test message"}'
