#!/usr/bin/env bash
!/usr/bin/env bash
#!/usr/bin/env bash

# statsd.sh

# Spins up three statsd containers in a cluster and outputs the IP Address of the first node

function statsd_start() {
    if [ ! "$(docker ps -q -f name=consul)" ]; then
        source Consul/consul_docker.sh start
    fi
    docker run -d\
         --name statsd\
         --rm\
         -p 80:80\
         -p 2003-2004:2003-2004\
         -p 2023-2024:2023-2024\
         -p 8125:8125/udp\
         -p 8126:8126\
         hopsoft/graphite-statsd
}

function statsd_stop() {
	docker stop statsd
}

function statsd_kill() {
	statsd_stop
	docker rm statsd
}

case "$1" in
	start)
		statsd_start
		;;
	stop)
		statsd_stop
		;;
	kill)
		statsd_kill
		;;
	*)
	 	echo "USAGE: statsd_docker.sh start|stop|kill"
		;;

esac