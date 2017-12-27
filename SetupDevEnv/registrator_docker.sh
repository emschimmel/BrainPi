#!/usr/bin/env bash

function registrator_start() {
    if [ ! "$(docker ps -q -f name=consul)" ]; then
        source consul_docker.sh start
    fi
    if [ ! "$(docker ps -q -f name=registrator)" ]; then
        docker run -d --rm --name=registrator --net=host -h registrator \
         --volume=/var/run/docker.sock:/tmp/docker.sock gliderlabs/registrator:latest consul://127.0.0.1:8500
    fi
}

function registrator_stop() {
	docker stop registrator
}

function registrator_kill() {
	registrator_stop
	docker rm registrator
}

case "$1" in
	start)
		registrator_start
		;;
	stop)
		registrator_stop
		;;
	kill)
		registrator_kill
		;;
	*)
	 	echo "USAGE: registrator_docker.sh start|stop|kill"
		;;

esac