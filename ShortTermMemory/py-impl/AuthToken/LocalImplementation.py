from collections import defaultdict

class LocalImplementation():

    tokenMemory = defaultdict(list)

    @classmethod
    def get(self, key):
        print('local get')
        return self.tokenMemory.get(key)

    @classmethod
    def put(self, key, value):
        print('local put')
        self.tokenMemory[key] = value

    @classmethod
    def delete(self, key):
        print('local delete')
        del self.tokenMemory[key]