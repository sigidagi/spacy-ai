#!/usr/bin/env python

from spacy.tokens import DocBin
import spacy
#from tqdm import tqdm

from spacy.pipeline.textcat_multilabel import DEFAULT_MULTI_TEXTCAT_MODEL

from data import dataset


def reset():
    """
    Reset all labels
    """
    categories = {
        'get_devices':0,
        'bind_devices':0,
        'change_name':0,
        'get_humidity':0,
        'get_pressure':0,
        'get_temperature':0
    }

    return categories


config = {
   "threshold": 0.5,
   "model": DEFAULT_MULTI_TEXTCAT_MODEL,
}

nlp = spacy.blank("en") # load a new spacy model
nlp.add_pipe("textcat_multilabel", config=config)

db = DocBin() # create a DocBin object

def add_document(sentence, category):
    """
    Add sentence to training set and provide sentence category(label)
    """
    doc = nlp.make_doc(sentence)
    doc.cats = reset()
    doc.cats[category] = 1
    #print("Sentence {}".format(sentence))
    #print("Cats {}", doc.cats)
    db.add(doc)


def convert2(outfile):
    """
    Converts trainig dataset to .spacy and saves to privided
    'outfile'
    """
    category_list = ['get_devices', 'bind_devices', 'change_name', 'get_humidity', 'get_pressure', 'get_temperature']
    for category in category_list:
        for sentence in dataset.data[category]:
            add_document(sentence, category)

    db.to_disk(outfile)


# ------------- START -------------
convert2("./data/train.spacy")
