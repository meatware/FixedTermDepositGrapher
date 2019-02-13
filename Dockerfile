FROM python:3.6-alpine

RUN apk add --no-cache screen py3-setuptools vim bash && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    ln -sf /usr/bin/python3 /usr/bin/python && \
    rm -r /root/.cache

WORKDIR /workspace

RUN adduser --shell /bin/bash --disabled-password --gecos "" --uid 1500 panda

RUN chown -R panda:panda /workspace

# set path to pip install --user
ENV PATH="/home/firmstep/.local/bin:${PATH}"

USER panda

CMD tail -f /dev/null
