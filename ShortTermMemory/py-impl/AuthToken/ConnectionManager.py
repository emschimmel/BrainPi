import sys
sys.path.append('../../')
import config
from . import RedisImplementation
from . import LocalImplementation

class State_d:
    def __init__(self, imp):
        self.__implementation = imp
    def changeImp(self, newImp):
        self.__implementation = newImp
    # Delegate calls to the implementation:
    def __getattr__(self, name):
        return getattr(self.__implementation, name)

class ConnectionManager():

    try:
        import redis
        r = redis.StrictRedis(host=config.redis_service_ip, port=config.redis_service_port, db=0)
        r.ping()
        storage = State_d(RedisImplementation.RedisImplementation())
    except Exception:
        storage = State_d(LocalImplementation.LocalImplementation())

    def get(self, key):
        self.storage.get(key)

    def put(self, key, value):
        self.storage.put(key, value)

    def delete(self, key):
        self.storage.delete(key)


