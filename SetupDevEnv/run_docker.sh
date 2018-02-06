#!/usr/bin/env bash
sh Consul/consul_docker.sh start
sh registrator_docker.sh start
sh Redis/redis_docker.sh start
sh ElasticSearch/elastic_docker.sh start
sh Mongo/mongo_docker.sh start
#sh statsd_docker.sh start
