import sys
sys.path.append('../../')
import config
import redis


class RedisImplementation():

    def __init__(self):
        self.redisService = redis.StrictRedis(host=config.redis_service_ip, port=config.redis_service_port, db=0)


    def get(self, key):
        print('redis get')
        return self.redisService.get(key)

    # Redis docs:
    # - ex = expiretime in seconds
    # - px = expiretime in miliseconds
    def put(self, key, value):
        print('redis put')
        self.redisService.set(key, value, ex=config.max_token_time_seconds)

    def delete(self, key):
        print('redis delete')
        self.redisService.delete(key)
