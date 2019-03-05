#!/bin/bash

source ./.makefile/docker-userid.sh

docker-compose rm --force
docker rmi -f fixedtermdepositgrapher_app

docker network rm fixedtermdepositgrapher_default
docker volume prune --force # make more selective
