#!/bin/sh
#ENDPOINT=$1
FILE=$1

if [ $# != 1 ]; then
    echo "Provide one arguments: test file."
    exit 1
fi

#curl -s -X POST -H "Content-Type: application/json" http://127.0.0.1:7000/"${ENDPOINT}" -d @"${FILE}" | jq .
curl -s -X POST -H "Content-Type: application/json" http://khadas.local:7000/spacy -d @"${FILE}" | jq .
