import sys
sys.path.append('../../')
import config
import redis

class UserStorageRedis:


    __redisService = redis.StrictRedis(host=config.redis_service_ip, port=config.redis_service_port, db=0)

    def __init__(self):
        pass

    @classmethod
    def get(self, key):
        print('Common/Storage: redis get')
        return self.__redisService.get(key)

    # Redis docs:
    # - ex = expiretime in seconds
    # - px = expiretime in miliseconds
    @classmethod
    def put(self, key, value):
        print('Common/Storage: redis put')
        self.__redisService.set(key, value=value)

    @classmethod
    def delete(self, key):
        print('Common/Storage: redis delete')
        self.__redisService.delete(key)

    @classmethod
    def update(self, key, field, value):
        storedObject = self.get(key=key)
        if storedObject:
            storedObject[field] = value
            self.put(key, storedObject)
