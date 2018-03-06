#!/usr/bin/env bash

function rabbit_start() {
    if [ ! "$(docker ps -q -f name=consul)" ]; then
        source ../Consul/consul_docker.sh start
        # source ../registrator_docker.sh start
    fi
    if [ ! "$(docker ps -q -f name=rabbitmq)" ]; then
        docker run -v db:/usr/share/rabbitmq/data:rw --rm -d \
          --hostname my-rabbit \
          -p 5672:35672 --name rabbitmq rabbitmq:latest
    fi
}

function rabbit_stop() {
	docker stop rabbitmq
}

function rabbit_kill() {
	rabbit_stop
	docker rm rabbitmq
}

case "$1" in
	start)
		rabbit_start
		;;
	stop)
		rabbit_stop
		;;
	kill)
		rabbit_kill
		;;
	*)
	 	echo "USAGE: rabbit_docker.sh start|stop|kill"
		;;

esac