#!/bin/bash

IMAGES=$(docker-compose images)
docker-compose rm --force # this seems too general stx shit
docker rmi -f $IMAGES

docker network prune --force # make more selective or poss not if localised to a directory
docker volume prune --force # make more selective
