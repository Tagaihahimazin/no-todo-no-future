# no-todo-no-future

- tagai
- shu
- honda2
- ikeda
- よろしくお願いいたします。
- cpy許すまじ
- PIEN


## Djangoプロジェクトの作成・設定

```
# Djangoプロジェクトの生成
$ sudo docker-compose run web django-admin.py startproject composeexample .
```

### django_docker/settng.py
django_docker/setting.pyのDATABASEの部分を編集し，MySQLのコンテナに接続
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_docker',
        'USER': 'root',
        'HOST': 'db',
        'POST': 33306
    }
}
```
## 起動・ログイン

```
# アプリケーション立ち上げ
$ sudo docker-compose up

# コンテナにログイン（別ターミナルで）
$ sudo docker-compose exec web /bin/bash
```

## アクセス方法

```
localhost:18000
```

## databaseがないとき
下記コマンドを叩いた後、

```
python manage.py sqlmigrate polls 0001
python manage.py migrate
```

## databaseの1146エラー（テーブルがありません）対策
下記コマンドを叩く。
```
python manage.py makemigrations testpredict
python manage.py migrate
## 管理者アカウントの追加

```

python manage.py createsuperuser

```


##  

```
>>> from polls.models import Choice, Question

>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())
>>> q.save()

>>> q.question_text = "What's up?"
>>> q.save()

>>> current_year = timezone.now().year

>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()

>>> q = Question.objects.get(pk=1)

>>> q.choice_set.create(choice_text='Not much', votes=0)
>>> q.choice_set.create(choice_text='The sky', votes=0)

>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)
>>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()

```
