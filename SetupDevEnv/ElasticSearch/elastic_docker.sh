#!/usr/bin/env bash

function elastic_start() {
    if [ ! "$(docker ps -q -f name=consul)" ]; then
        source ../Consul/consul_docker.sh start
        # source ../registrator_docker.sh start
    fi
    if [ ! "$(docker ps -q -f name=elasticsearch)" ]; then
        docker run -v db:/usr/share/elasticsearch/data:rw --rm -d \
         -p 9200:32781 -p 9300:32780 --name elasticsearch elasticsearch:latest
    fi
}

function elastic_stop() {
	docker stop elasticsearch
}

function elastic_kill() {
	elastic_stop
	docker rm elasticsearch
}

case "$1" in
	start)
		elastic_start
		;;
	stop)
		elastic_stop
		;;
	kill)
		elastic_kill
		;;
	*)
	 	echo "USAGE: elastic_docker.sh start|stop|kill"
		;;

esac