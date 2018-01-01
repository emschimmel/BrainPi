from collections import defaultdict

class LocalImplementation():

    tokenMemory = defaultdict(list)

    @classmethod
    def get(self, key):
        print('ShortTermMemory: local get')
        return self.tokenMemory.get(key)

    @classmethod
    def put(self, key, value):
        print('ShortTermMemory: local put')
        self.tokenMemory[key] = value

    @classmethod
    def delete(self, key):
        print('ShortTermMemory: local delete')
        del self.tokenMemory[key]