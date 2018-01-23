#!/usr/bin/env bash

function redis_start() {
    if [ ! "$(docker ps -q -f name=consul)" ]; then
        source ../Consul/consul_docker.sh start
        # source ../registrator_docker.sh start
    fi
    if [ ! "$(docker ps -q -f name=redis)" ]; then
        docker run -v db:/data:rw --rm -d \
         -p 6379:32775 --name redis redis:latest
    fi
}

function redis_stop() {
	docker stop redis
}

function redis_kill() {
	redis_stop
	docker rm redis
}

case "$1" in
	start)
		redis_start
		;;
	stop)
		redis_stop
		;;
	kill)
		redis_kill
		;;
	*)
	 	echo "USAGE: redis_docker.sh start|stop|kill"
		;;

esac