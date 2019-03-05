FROM python:3.6-alpine

ARG USER_ID

RUN apk add --no-cache screen vim bash nano

RUN adduser --shell /bin/bash --disabled-password --gecos "" --uid $USER_ID panda

ADD . /workspace
WORKDIR /workspace

RUN chown -R panda:panda /workspace

USER panda
# set path to pip install --user
ENV PATH="/home/panda/.local/bin:${PATH}"

RUN pip install -r requirements.txt --user

CMD tail -f /dev/null
