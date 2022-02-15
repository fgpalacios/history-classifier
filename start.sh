#!/bin/bash
app="docker.publications.class_dt_v1"
docker build -t ${app} .
docker run -d -p 8884:80 \
  --name=${app} \
  -v $PWD:/app ${app}
