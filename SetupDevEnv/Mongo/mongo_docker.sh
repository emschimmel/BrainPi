#!/usr/bin/env bash

function mongo_start() {
    if [ ! "$(docker ps -q -f name=consul)" ]; then
        source ../consul_docker.sh start
        # source ../registrator_docker.sh start
    fi
    if [ ! "$(docker ps -q -f name=mongo)" ]; then
        docker run -v db:/data/db:rw --rm -d \
         -p 32776:27017 --name mongo mongo:latest
    fi
}

function mongo_stop() {
	docker stop mongo
}

function mongo_kill() {
	mongo_stop
	docker rm mongo
}

case "$1" in
	start)
		mongo_start
		;;
	stop)
		mongo_stop
		;;
	kill)
		mongo_kill
		;;
	*)
	 	echo "USAGE: mongo_docker.sh start|stop|kill"
		;;

esac