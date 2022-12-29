curl https://api.openai.com/v1/images/generations \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "prompt": "Chinese New Year in 2023",
    "n": 1,
    "size": "256x256"
  }'
