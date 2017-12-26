import sys

sys.path.append('../../')
import config

# import importlib
# spam_spec = importlib.util.find_spec("redis")
# found = spam_spec is not None
# print(found)

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
    except ImportError:
        redis = None
    if redis:
        try:
            r = redis.StrictRedis(host=config.redis_service_ip, port=config.redis_service_port, db=0)
            r.ping()
            from . import RedisImplementation
            storage = State_d(RedisImplementation.RedisImplementation())
        except Exception as ex:
            from . import LocalImplementation
            storage = State_d(LocalImplementation.LocalImplementation())
    else:
        from . import LocalImplementation
        storage = State_d(LocalImplementation.LocalImplementation())

    def get(self, key):
        return self.storage.get(key)

    def put(self, key, value):
        self.storage.put(key, value)

    def delete(self, key):
        self.storage.delete(key)


