from django.contrib.auth.models import User

class AppBackends(object):
    def authenticate(self, token = None ):
        # TODO: do auth
        try:
            user = User.objects.get(token = token)
        except User.DoesNotExist:
            return None
        return user


    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def has_perm(self,user_obj, perm, obj = None):
        return True

