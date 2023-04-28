#!/bin/sh

python train.py
sleep 1
python -m spacy train ./configs/config.cfg --output ./data/output --paths.train ./data/train.spacy --paths.dev ./data/train.spacy

