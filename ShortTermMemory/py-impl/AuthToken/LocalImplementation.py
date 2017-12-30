from collections import defaultdict

class LocalImplementation():

    tokenMemory = defaultdict(list)

    def get(self, key):
        print('local get')
        return self.tokenMemory.get(key)

    def put(self, key, value):
        print('local put')
        self.tokenMemory[key] = value

    def delete(self, key):
        print('local delete')
        del self.tokenMemory[key]