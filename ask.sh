#!/bin/sh
ENDPOINT=$1
FILE=$2

if [ $# != 2 ]; then
    echo "Provide two arguments: 1. test endpoint 2. test file."
    echo "Endpoints are: 'spacy'"
    exit 1
fi

curl -s -X POST -H "Content-Type: application/json" http://127.0.0.1:7000/"${ENDPOINT}" -d @"${FILE}" | jq .
