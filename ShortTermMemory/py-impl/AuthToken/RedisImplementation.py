import redis
import sys
sys.path.append('../../')
import config

class RedisImplementation():

    def __init__(self):
        self.redisService = redis.StrictRedis(host=config.redis_service_ip, port=config.redis_service_port, db=0)


    def get(self, key):
        print('redis get')
        return self.redisService.get(key)

    def put(self, key, value):
        # self.max_token_time
        # TODO: use the ttl
        print('redis put')
        # ex = expiretime in seconds
        # px = expiretime in miliseconds
        self.redisService.set(key, value, ex=config.max_token_time_seconds)

    def delete(self, key):
        print('redis delete')
        self.redisService.delete(key)
