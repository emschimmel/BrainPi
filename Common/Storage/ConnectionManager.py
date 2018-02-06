import sys

sys.path.append('../')
import config

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
            from . import UserStorageRedis
            storage = State_d(imp=UserStorageRedis.UserStorageRedis())
        except Exception as ex:
            from . import UserStorageLocal
            storage = State_d(imp=UserStorageLocal.UserStorageLocal())
    else:
        from . import UserStorageLocal
        storage = State_d(imp=UserStorageLocal.UserStorageLocal())

    def get(self, key):
        return self.storage.get(key=key)

    def put(self, key, value):
        self.storage.put(key=key, value=value)

    def update(self, key, field, value):
        self.storage.update(key=key, field=field, value=value)

    def delete(self, key):
        self.storage.delete(key=key)


