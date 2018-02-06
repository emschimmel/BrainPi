from UserProvider import UserProvider
from Storage.ConnectionManager import ConnectionManager
from configparser import ConfigParser

class ConnectionUtil:
    parser = ConfigParser()
    parser.read('config.ini')

    def connect(self, service, uniquename, context):
        key, user = UserProvider().get_user(service=service, uniquename=uniquename, context=context)
        if user.acces_token is None:
            token = self.get_acces_token(service)
            ConnectionManager().update(key=key, field='acces_token', value=token)


    def user_login(self, service):

        app_id = self.parser.get(service, 'api_id')
        redirect_uri = self.parser.get(service, 'redirect_uri')
        perms = self.parser.get(service, 'perms')
        oauth_path = self.parser.get(service, 'oauth_path_1')
        # ("https://connect.deezer.com/oauth/auth.php?app_id=%s&redirect_uri=%s& perms=%s" % app_id % redirect_uri % oauth_path)
        request_url = oauth_path.format(app_id, redirect_uri, perms)

        pass

    def get_acces_token(self, service):
        code = self.user_login(service=service)
        app_id = self.parser.get(service, 'api_id')
        secret = self.parser.get(service, 'secret')
        oauth_path = self.parser.get(service, 'oauth_path_2')
        request_url = oauth_path.format(app_id, secret, code)
        pass

    def get_request_token(self):
        pass

if __name__ == '__main__':
    ConnectionUtil().connect(service='Deezer', uniquename='me', context=None)
