#!/usr/bin/env bash

PORT=8080
echo "Port: $PORT"

# POST method predict
curl -d '{  
    "model":"A1",
    "year":2017,
    "transmission":"Manual",
    "mileage":15735,
    "fuelType":"Petrol",
    "tax":150,
    "mpg":55.4,
    "engineSize":1.4,
    "manufacter":"Audi",
}'\
     -H "Content-Type: application/json" \
     -X POST http://localhost:$PORT/predict