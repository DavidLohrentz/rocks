#!/usr/bin/env bash

docker run --rm -ti -p 4000:80 \
-v /home/dloh/Documents/git_stuff/Modern_python/rock:/var/opt \
rocks
