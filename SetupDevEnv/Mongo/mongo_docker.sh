#!/usr/bin/env bash

function mongo_start() {
    if [ ! "$(docker ps -q -f name=consul)" ]; then
        source ../consul_docker.sh start
        # source ../registrator_docker.sh start
    fi
    if [ ! "$(docker ps -q -f name=mongo)" ]; then
        docker run -v db:/data/db:rw --rm -d \
         -p 27017:27017 --name mongo mongo:latest
    fi
}

function mongo_stop() {
	docker stop mongo
}

function mongo_kill() {
	mongo_stop
	docker rm mongo
}

function mongo_clean() {
    python3 mongo_clean.py
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
	clean)
		mongo_clean
		;;
	*)
	 	echo "USAGE: mongo_docker.sh start|stop|kill|clean"
		;;

esac