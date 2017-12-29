import random

from dns import resolver

class AppConfig:
    def resolve_config(self, host, port):
        consul_resolver = resolver.Resolver()
        consul_resolver.port = port
        consul_resolver.nameservers = [host]

        dnsanswer = consul_resolver.query("eye-pi.service.consul.", 'A')
        ip = str(dnsanswer[0])
        dnsanswer_srv = consul_resolver.query("eye-pi.service.consul.", 'SRV')
        port = int(str(random.choice(dnsanswer_srv)).split()[2])
        return ip, port
