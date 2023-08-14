#!/usr/bin/env python

from typing import Optional, List
import spacy
#import classy_classification
import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel

model_path = "./data/output/model-best"

#from data import dataset


# ---------- SpaCy NLP implementation ------------------

# nlp_spacy = spacy.load("en_core_web_sm")
nlp_spacy = spacy.load(model_path)


# nlp_spacy.add_pipe("text_categorizer",
             # config={
                 # "data": dataset.data,
                 # "model":
                 # "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
                 # "device": "gpu",
                 # "multi_label": True,
             # })
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
        #cats = nlp_spacy(utt.text)._.cats
        cats = nlp_spacy(utt.text).cats
        categories.append(cats)
    return categories

if __name__ == "__main__":
    uvicorn.run("start_classifiers:app", port=7000, log_level="info")
