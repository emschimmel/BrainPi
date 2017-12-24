#!/usr/bin/env bash

function consul_start() {
    if [ ! "$(docker ps -q -f name=consul)" ]; then
        docker run --rm -d -p 8400:8400 -p 8500:8500 -p 8600:53/udp \
            --name consul1 -h consul1 progrium/consul -server \
            -bootstrap-expect 3 -ui-dir /ui
        JOIN_IP=$(docker inspect -f '{{.NetworkSettings.IPAddress}}' consul1)
        docker run --rm -d --name consul2 -h consul2 progrium/consul -server -join $JOIN_IP
        docker run --rm -d --name consul3 -h consul3 progrium/consul -server -join $JOIN_IP

        echo "Consul IP: $JOIN_IP"
        echo "Visit: http://127.0.0.1:8500/ui"
    fi
}

function consul_stop() {
	docker stop consul1 consul2 consul3
}

function consul_kill() {
	consul_stop
	docker rm consul1 consul2 consul3
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