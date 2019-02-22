FROM python:3.6-alpine

ADD . /workspace
WORKDIR /workspace

RUN adduser --shell /bin/bash --disabled-password --gecos "" --uid 1500 panda

RUN chown -R panda:panda /workspace

# set path to pip install --user
#ENV PATH="/home/firmstep/.local/bin:${PATH}"

RUN pip install -r requirements.txt
#RUN pip install -r dev-requirements.txt

USER panda

CMD tail -f /dev/null
