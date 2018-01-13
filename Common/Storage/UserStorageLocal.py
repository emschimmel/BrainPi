from collections import defaultdict

class UserStorageLocal:

    userMemory = defaultdict(list)

    @classmethod
    def get(self, key):
        print('Common/Storage: local get')
        return self.userMemory.get(key)

    @classmethod
    def put(self, key, value):
        print('Common/Storage: local put')
        self.userMemory[key] = value

    @classmethod
    def delete(self, key):
        print('Common/Storage: local delete')
        del self.userMemory[key]

    @classmethod
    def update(self, key, field, value):
        storedValue = self.get(key=key)
        storedValue[field] = value
        self.put(key, storedValue)
