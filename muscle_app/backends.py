# from django.contrib.auth import get_user_model
from .models import Users_list
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()
# UserModel = Users_list.objects.all()

class EmailAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **credentials):
        # UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user