from django.contrib.auth.models import User
from django.contrib.auth.backends import BaseBackend

class EmailAuthBackend(BaseBackend):
    print("in email backend")
    def authenticate(self, request, username, password):
        try:
            user = User.objects.get(email=username)
            print("user: ", user)
            is_password_ok = user.check_password(password)
            if is_password_ok:
                print("email: ", username)
                print("password: ", password)
                return user
        except User.DoesNotExist:
            pass
        return None
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
