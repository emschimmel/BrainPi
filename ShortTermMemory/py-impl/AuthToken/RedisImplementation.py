import redis
import sys
sys.path.append('../../')
import config

class RedisImplementation():

    max_token_time = 1000

    def __init__(self):
        self.redisService = redis.StrictRedis(host=config.redis_service_ip, port=config.redis_service_port, db=0)


    def get(self, key):
        print('redis get')
        return self.redisService.get(key)

    def put(self, key, value):
        # self.max_token_time
        # TODO: use the ttl
        print('redis put')
        self.redisService.set(key, value)

    def delete(self, key):
        print('redis delete')
        self.redisService.delete(key)
