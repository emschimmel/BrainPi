#!/usr/bin/env bash
./consul_docker.sh stop
./registrator_docker.sh stop
./statsd_docker.sh stop
cd ./Mongo/
    ./mongo_docker.sh stop
cd ..

cd ./Redis/
    ./redis_docker.sh stop
cd ..

cd ./ElasticSearch/
    ./elastic_docker.sh stop
cd ..

