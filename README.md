# susie-nick
筋トレメニュー共有サイト

### ver.1.1の変更点
DBのテーブル情報を変更しました。
ログインの際、@のあとにuseridを入力することでuseridでのログインをできるようにしました。
トップ画面の検索ボックスを使用しての検索機能の追加。現在はuseridとタイトルでのみ絞り込みが可能。
記事編集の際、タイトルの文字数オーバーや、記事内容に空白、改行のみで登録された際にエラーを表示するようにしました。
部位ごとの記事表示の際、同じ処理をそれぞれの部位ごとに分けていたのを統合し、viewsを整理。それに伴いTemplateも整理しました。
その他、views、Template、formsなどの内容を整理しました。

### ver.1.1.2の変更点
docker-compose.ymlの変数を外部ファイルから読み込むようにし、gitignoreから除外し、公開しました。
また、Dockerfileに機密情報が含まれていないため、gitignoreから除外し、公開しました。
ユーザー情報変更の機能を正常に動くようにしました。また、それに伴いDBのテーブル情報を少し変更しました。
DBのmigrateがうまくいかないため、migrationsフォルダをgithubの追跡対象として追加しました。
記事の新規登録の際、ログインしているかのチェックを記事送信時ではなく、ページ遷移時に変更しました。
記事の編集、削除を自分の記事一覧からのみ行えるように変更しました。
