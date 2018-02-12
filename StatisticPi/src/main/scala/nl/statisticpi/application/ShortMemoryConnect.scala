package nl.statisticpi.application

import java.util.concurrent.TimeUnit

import akka.actor.ActorSystem
import akka.discovery.ServiceDiscovery
import akka.discovery.SimpleServiceDiscovery.Resolved

import scala.concurrent.Future
import scala.concurrent.duration.FiniteDuration

class ShortMemoryConnect  {

    class ServiceAddress(ip: String, port: String) {

    }

    def make_data_request(): Unit = {
        val config: Future[Resolved] = get_config()
//        config.onComplete {
//            case Success(data) => println(data)
//        }

    }

    def get_config(): Future[Resolved] = {
        val system = ActorSystem("Example")
        val discovery = ServiceDiscovery(system).discovery
        val finiteDuration = new FiniteDuration(500, TimeUnit.MILLISECONDS)
        discovery.lookup(name = "short-term-memory.service.consul.", resolveTimeout = finiteDuration)
    }

}
