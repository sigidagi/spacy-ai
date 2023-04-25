#!/bin/sh
curl -s -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/sentence -d @sentence.json | jq .
