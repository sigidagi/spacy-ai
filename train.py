#!/usr/bin/env python
"""
File for converting json datasets: training and validation to spacy binary format.
"""

from enum import Enum
from spacy.tokens import DocBin
import spacy

from spacy.pipeline.textcat_multilabel import DEFAULT_MULTI_TEXTCAT_MODEL

from data import dataset
from data import devset

class Set(Enum):
    """
    Defines if data set if trainig or validation set
    """
    VALIDATION = 1
    TRAINING = 2

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
        'get_temperature':0,
        'not_implemented':0,
        'out_of_scope':0,
    }

    return categories


config = {
   "threshold": 0.5,
   "model": DEFAULT_MULTI_TEXTCAT_MODEL,
}

nlp = spacy.blank("en") # load a new spacy model
nlp.add_pipe("textcat_multilabel", config=config)


def add_category(sentence, category):
    """
    Add sentence to training set and provide sentence category(label)
    """
    doc = nlp.make_doc(sentence)
    doc.cats = reset()
    doc.cats[category] = 1
    return doc


def convert_tobin(outfile, settype):
    """
    Converts trainig dataset to .spacy and saves to privided
    'outfile'
    """
    doc_bin = DocBin() # create a DocBin object
    category_list = [
            'get_devices',
            'bind_devices',
            'change_name',
            'get_humidity',
            'get_pressure',
            'get_temperature',
            'not_implemented',
            'out_of_scope',
    ]
    for category in category_list:
        if settype == Set.TRAINING:
            for sentence in dataset.data[category]:
                doc = add_category(sentence, category)
                doc_bin.add(doc)
        else:
            for sentence in devset.data[category]:
                doc = add_category(sentence, category)
                doc_bin.add(doc)

    doc_bin.to_disk(outfile)


# ------------- START -------------
# trining set
convert_tobin("./data/train.spacy", Set.TRAINING)
# validation set
convert_tobin("./data/dev.spacy", Set.VALIDATION)
