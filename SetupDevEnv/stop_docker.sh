#!/usr/bin/env bash
sh Consul/consul_docker.sh stop
sh registrator_docker.sh stop
sh Mongo/mongo_docker.sh stop
sh Redis/redis_docker.sh stop
sh ElasticSearch/elastic_docker.sh stop
sh statsd_docker.sh stop

