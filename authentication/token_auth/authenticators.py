from django.utils.translation import gettext_lazy as _
from rest_framework import authentication as rf_auth
from rest_framework import exceptions
from rest_framework.authtoken.models import Token
from base_app import settings
import datetime


# Extends basic Token Authentication to enable token expiry
# Note change in settings module authenticators
class TokenAuthentication(rf_auth.TokenAuthentication):

    def _create_token(user):
        return Token.objects.create(user=user)

    def _token_expired(self, token_created):
        # Get token age in seconds. See python datetime API for details
        token_age = (datetime.datetime.now(datetime.timezone.utc)
                     - token_created).seconds
        if token_age > settings.REST_FRAMEWORK['TOKEN_EXPIRY_TIME_SEC']:
            return True
        return False

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

        if self._token_expired(token.created):
            token.delete()
            raise exceptions.AuthenticationFailed(_('Token has expired.'))

        return (token.user, token)
