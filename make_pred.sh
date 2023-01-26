#!/usr/bin/env bash

PORT=5000
echo "Port: $PORT"

# POST method predict
curl -d '{  
   "filename":"test.csv"
}'\
     -H "Content-Type: application/json" \
     -X POST http://localhost:$PORT/predict