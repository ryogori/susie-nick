# 記事投稿の際、空文字を送信した場合に発生するエラークラスを作成。
class ValueNoneError(Exception):
    pass