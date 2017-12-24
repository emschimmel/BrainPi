#!/usr/bin/env bash
./consul_docker.sh start
./registrator_docker.sh start
# ./statsd_docker.sh start
cd ./Mongo/
    ./mongo_docker.sh start
cd ..

cd ./Redis/
    ./redis_docker.sh start
cd ..

cd ./ElasticSearch/
    ./elastic_docker.sh start
cd ..

