#!/usr/bin/env python

from typing import Optional, List
import spacy
import classy_classification
import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel

import dataset


# ---------- SpaCy NLP implementation ------------------

nlp_spacy = spacy.blank("en")
nlp_spacy.add_pipe("text_categorizer",
             config={
                 "data": dataset.data,
                 "model":
                 "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
                 "device": "gpu",
                 "multi_label": True,
             })
# ----------------------------------------------------

class Utterance(BaseModel):
    """
    Acceptecd incomming model
    """
    text: str
    intent: Optional[str] = None

app = FastAPI()

@app.get("/")
async def root():
    """
    Just a REST test
    """
    return [{"message": "Hello", "intent": "World"}]

@app.post("/spacy")
async def sentence(utterances: List[Utterance]):
    """
    test sentencies for SpaCy classifier
    """
    categories = []
    for utt in utterances:
        cats = nlp_spacy(utt.text)._.cats
        categories.append(cats)
    return categories


if __name__ == "__main__":
    uvicorn.run("start_classifiers:app", port=5000, log_level="info")
