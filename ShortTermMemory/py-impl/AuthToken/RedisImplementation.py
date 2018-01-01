import sys
sys.path.append('../../')
import config
import redis


class RedisImplementation():

    __redisService = redis.StrictRedis(host=config.redis_service_ip, port=config.redis_service_port, db=0)

    def __init__(self):
        pass

    @classmethod
    def get(self, key):
        print('redis get')
        return self.__redisService.get(key)

    # Redis docs:
    # - ex = expiretime in seconds
    # - px = expiretime in miliseconds
    @classmethod
    def put(self, key, value):
        print('redis put')
        self.__redisService.set(key, value=value, ex=config.max_token_time_seconds)

    @classmethod
    def delete(self, key):
        print('redis delete')
        self.__redisService.delete(key)
