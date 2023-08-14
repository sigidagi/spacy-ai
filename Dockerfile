FROM python:3.9
MAINTAINER Sigitas Dagilis
RUN echo 'we are running some # AI - classy classifier!'

WORKDIR /home
RUN apt-get update

COPY out_of_scope.txt .
COPY ask.sh .
COPY requirements.txt . 
COPY start_classifiers.py . 
COPY train.py . 
COPY train.sh . 
COPY configs/ ./configs/
COPY data/output/model-best/ ./data/output/model-best/
COPY test/ ./test/

RUN ls --recursive ${WORKDIR}

RUN pip install -r requirements.txt

CMD ["python", "/home/start_classifiers.py"]
#ENTRYPOINT ["tail"]
#CMD ["-f","/dev/null"]
