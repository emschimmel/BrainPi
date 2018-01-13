
from Storage.ConnectionManager import ConnectionManager


class UserProvider:

    def get_user(self, service, uniquename, context=None):
        key = self.generate_key(service=service, uniquename=uniquename)
        user = ConnectionManager().get(key)
        if user is None:
            user = UserModel(service, uniquename, context)
            ConnectionManager().put(key, user)
        return key, user

    @staticmethod
    def generate_key(service, uniquename):
        return '%s:%s' % (service, uniquename)


class UserModel(object):
    uniquename = ''
    service = ''
    context = ''
    acces_token = None
    request_token = None
    refresh_token = None

    def __init__(self, uniquename, service, context=None):
        self.uniquename = uniquename
        self.service = service
        self.context = context

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        return setattr(self, key, value)