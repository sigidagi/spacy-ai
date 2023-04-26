#!/usr/bin/env python

import spacy
import classy_classification
import uvicorn
import dataset

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


nlp_spacy = spacy.blank("en")
nlp_spacy.add_pipe("text_categorizer",
             config={
                 "data": dataset.data,
                 "model":
                 "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
                 "device": "gpu",
                 "multi_label": True,
             })


class Utterance(BaseModel):
    text: str
    intent: Optional[str] = None

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/spacy")
async def sentence(utterance: Utterance):
    print(utterance.text)
    categories = nlp_spacy(utterance.text)._.cats
    return categories 


if __name__ == "__main__":
    uvicorn.run("start_classifiers:app", port=5000, log_level="info")
