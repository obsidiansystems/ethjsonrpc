##### NB: to run on an M1 Mac do:
##
## docker build --platform linux/amd64 -t poly . && docker run --platform linux/amd64 -it poly

FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y gcc virtualenv libssl-dev pip
RUN pip3 install requests ethereum

RUN mkdir workdir
WORKDIR /workdir
COPY ethjsonrpc ethjsonrpc

COPY poly.py ./
COPY test.py ./

RUN python3 poly.py
# the below will fail
RUN python3 test.py || true
