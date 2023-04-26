#!/bin/sh
curl -s -X POST -H "Content-Type: application/json" http://127.0.0.1:5000/spacy -d @sentence.json | jq .
