#!/usr/bin/env bash

function consul_start() {
    if [ ! "$(docker ps -q -f name=consul)" ]; then
        docker run --rm -d -p 8400:8400 -p 8500:8500 -p 8600:8600/udp \
            --name consul -h consul consul
        echo "Visit: http://127.0.0.1:8500/ui"
        if [ -f "first_device.py" ]; then
            python3 first_device.py
        else
            cd Consul
            python3 first_device.py
            cd ..
        fi
    fi
}

function consul_stop() {
	docker stop consul
}

function consul_kill() {
	consul_stop
	docker rm consul
}

case "$1" in
	start)
		consul_start
		;;
	stop)
		consul_stop
		;;
	kill)
		consul_kill
		;;
	*)
	 	echo "USAGE: consul_docker.sh start|stop|kill"
		;;

esac