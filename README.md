# susie-nick
筋トレメニュー共有サイト

## dockerの導入について
1, install.shがあるフォルダに行き、以下のコマンドを実行してインストール。

source install.sh
2, その後再起動

## 構築手順
1, projectを作成

sudo docker-compose run web python3 -m django startproject {#任意のプロジェクト名} .
2, プロジェクトフォルダ内にあるsettings.pyのDATABASESという項目を編集

vim settings.py
###### settings.pyの中身

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'muscle-db',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'db',
        'PORT': '3306'
    }
}
3, 各サービスを起動

docker-compose up -d
4, 起動確認
> http://localhost:8000
に接続して、ウェルカムページが表示されるか確認。
