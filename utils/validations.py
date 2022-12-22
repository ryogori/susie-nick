from django.core.exceptions import ValidationError
import re

class CustomPasswordValidator():
    msg = 'パスワードには、大文字英字、小文字英字、数字、記号(-@^#$(){}[]!?*&=)をそれぞれ1つ以上含めてください。'

    def __init__(self):
        pass

    def validate(self, password, user=None):
        if all(
            (re.search('[A-Z]', password),
            re.search('[a-z]', password),
            re.search('[0-9]', password),
            re.search('[-@^#$!?*&=\(\)\{\}\[\]]', password),)):
            return
        raise ValidationError(self.msg)

    def get_help_text(self):
        return self.msg
        