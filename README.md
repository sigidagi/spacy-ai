## Installation

Create python virtual environment and install dependencies

```
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Training

[Spacy quickstart](https://spacy.io/usage/training#quickstart)


```
./train.sh
```

It will use 'data/dataset.py' to create pre-trained model 

## Run

```
./start_classifiers.py
```

## Test


```
./ask.sh spacy ./test/temperature.json
```


