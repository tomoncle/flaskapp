#!/usr/bin/env bash

cd ../
find flaskapp -name *.pyc|xargs rm -rf

cd -
docker build -t tomoncle/flaskapp .
docker push tomoncle/flaskapp