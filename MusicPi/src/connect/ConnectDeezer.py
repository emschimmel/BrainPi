# http://python-social-auth.readthedocs.org/
# https://github.com/python-social-auth/social-examples

from social_core.backends.deezer import DeezerOAuth2
from social_core.backends.utils import load_backends


from configparser import ConfigParser

import re
from social_core.backends.oauth import OAuthAuth

# NAME_RE = re.compile(r'([^O])Auth')
DEEZER_BACKEND_CONFIG = 'social_core.backends.deezer.DeezerOAuth2'


parser = ConfigParser()
parser.read('../config/deezer.ini')
API_KEY = parser.get('DEFAULT', 'apikey')
API_SECRET = parser.get('DEFAULT', 'apisecret')
USERNAME = parser.get('DEFAULT', 'username')


class ConnectDeezer:
    def try_to_connect(self):
        DeezerOAuth2.start()
    pass


# class AppBaseView():
#     def render_home(self, **extra):
#         context = common_context(
#             DEEZER_BACKEND_CONFIG,
#             load_strategy(),
#             user=self.get_current_user(),
#             plus_id=API_KEY,
#             **extra
#         )
# # return render.home(**context)
#
# def is_authenticated(user):
#     if callable(user.is_authenticated):
#         return user.is_authenticated()
#     else:
#         return user.is_authenticated
#
# def associations(user, strategy):
#     user_associations = strategy.storage.user.get_social_auth_for_user(user)
#     if hasattr(user_associations, 'all'):
#         user_associations = user_associations.all()
#     return list(user_associations)
#
# def common_context(authentication_backends, strategy, user=None, **extra):
#     """Common view context"""
#     context = {
#         'user': user,
#         'available_backends': load_backends(authentication_backends),
#         'associated': {}
#     }
#
#     if user and is_authenticated(user):
#         context['associated'] = dict((association.provider, association)
#                                      for association in associations(user, strategy))
#
#     return dict(context, **extra)

if __name__ == '__main__':
    ConnectDeezer()
