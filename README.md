## Installation




Create python virtual environment and install dependencies

```
python -m venv .venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Training

Dataset are saved into file `data/dataset.py` so it is loaded from training program `train.py`


[Spacy quickstart](https://spacy.io/usage/training#quickstart)


```
./train.sh
```

It will use 'data/dataset.py' to create pre-trained model 

## Run

```
./start_classifiers.py
```

### Docker
```
docker build . -t classy-ai
docker run -dit -p 7000:7000 classy-ai 
docker exec -it <container-name> bash
```

## Test

```
./ask.sh spacy ./test/temperature.json
```

or 
```
curl -s -X POST -H "Content-Type: application/json" http://127.0.0.1:7000/spacy -d '[{"text": "How cold is it in my room?"}]'
```


