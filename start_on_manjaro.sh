#!/usr/bin/env bash

docker run --rm -ti -p 4000:80 \
-v /home/davidl/Documents/projects/rocks:/var/opt \
rocks
