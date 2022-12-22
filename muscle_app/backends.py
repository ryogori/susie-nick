from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()

# Useridでの認証
class UseridAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **credentials):
        try:
            # ユーザーが存在するか確認。存在している場合、パスワードのチェックを行う。
            user = UserModel.objects.get(user_id=username)
        except UserModel.DoesNotExist:
            # ユーザーが存在しない場合、noneを返す。
            return None
        else:
            # ハッシュ化されたパスワードと、入力されたパスワードのハッシュ値が同じかを確認。認証された場合、ユーザーを返す。
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

# Emailでの認証
class EmailAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **credentials):
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user