FROM ubuntu:latest
LABEL Author="Noel Presti" Project="the-Big-SleePy"
USER root

VOLUME Python

RUN apt-get update && apt-get install -y python2

COPY ./python /Python

RUN chmod 700 -R /Python/

CMD ["/Python/shuffle.py"]
