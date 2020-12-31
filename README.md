# DjangoでWebアプリ作成（SQLite3）



## 仮想環境作成(venv)

ターミナルまたはパワーシェルで次の操作

1. 仮想環境  `venv` 作成のためのコマンド  
注意：Macの場合は python3としてください。

```
python -m venv dj_todo
```

2. `cd`コマンドで出来上がったフォルダ（ここではdj_todo）に移動

```
cd dj_todo
```

1. 以下の仮想環境を実行するコマンドを実行（MacとWindowsでコマンドは違うので注意）

#### Macの場合

Macで`venv` の仮想環境を実行するコマンド

```
source bin/activate
```

#### Windowsの場合

Windowsで`venv` の仮想環境を実行するコマンド

```
Scripts\activate
```

#### Windowsで仮想環境を実行時に出るエラー対策

`Scripts\activate`で**「PSSecurityException」**が発生する場合がる

この場合次のコマンド

```
Set-ExecutionPolicy RemoteSigned -Scope Process
```

実行ポリシーを聞かれたら、「Y」を入力してEnter

再び仮想環境に入る

```
Scripts\activate
```

### pip upgrade

```
python -m pip install --upgrade pip
```


仮想環境に入るとMacの場合でも、python3ではなくpythonコマンドが使えるようになります。

また、pipもpip3ではなくpipが使えるようになります。

バージョンなどを確認して正しくこれらのコマンドが使えるか確認してください。

```
python -V
```

```
pip -V
```



## Djangoのインストール

ターミナルまたはパワーシェルで次の操作

Djangoインストールコマンド  

```
pip install django
```

Djangoのバージョン確認コマンド  

```
python -m django --version
```



## TODOプロジェクト作成

ターミナルまたはパワーシェルで次の操作

1.  `venv` 仮想フォルダの中にプロジェクト用の新しいフォルダ「TODOPROJECT」を作成

2. コマンドの `cd` でカレントディレクトリを `TODOPROJECT` フォルダに移動します。

   ```
   cd TODOPROJECT
   ```

3. Djangoのプロジェクトを作成するコマンド

```
django-admin startproject todoproject .
```



### アプリケーションの作成

1. アプリケーション作成コマンド 
   ターミナルまたはパワーシェルで次の操作 

```
python manage.py startapp todo
```



## Gitの作成

「TODOPROJECT」フォルダ内をGit管理します。

TODOPROJECTフォルダ内に新規で` .gitignore` ファイルを作成して以下記述

GitHubにpushする場合、static/はpushしないように.gitignoreファイルに記述します。

ただし、HEROKUにpushする場合はこの記述を削除します。

```
*.pyc
__pycache__/
db.sqlite3
static/
```

以下コマンドを実行

ターミナルまたはパワーシェルで次の操作

```
git init
```

```
git add .
```

```
git commit
```

## Djangoの設定

### settings.pyの変更

#### import文の追加

1. 先頭にimport osを追加

```
import os
```

#### シークレットキーの設定

1. シークレットキーの情報をコピーして保存(この記述はサンプルです。自分の本当の値をコピーすること)

   ```
   SECRET_KEY = 'ei!mmcb3n(me^ww$&9xz3$r^xf+75_8^2x6_&38)^dti6338-t$=s'
   ```

2. シークレットキーの情報を環境変数に隠蔽
   環境変数の取り扱いは別途手順書を参照

```
SECRET_KEY = os.environ.get('SECRET_KEY_TODO')
```

3. MAC の場合、元々SECRET_KEYに記述されていた値をコピーして自分のPCの環境変数に貼り付け
   ZSHの場合：.zshrcをエディタで開いて下記貼り付け

   bashの場合：.bash_profileをエディタで開いて下記貼り付け

```
export SECRET_KEY_TODO='w0ni-ss@e13^v!dddwb59bug+g4h18-3h^*!sisden#bb@66+@ase'
```

​		**一度deactivateして必ずターミナルを再起動してくだい。**
​		Macで`venv` の仮想環境を実行するコマンド

```
source bin/activate
```

4. Windowsの場合、システムの「環境変数を編集」からユーザー環境変数で新規を選ぶ
   変数名：SECRET_KEY_TODO
   変数値：'w0ni-ss@e13^v!dddwb59bug+g4h18-3h^*!sisden#bb@66+@ase'

   その後、コマンド `deactivate` で仮想環境を出てから**PowerShellを再起動**
   再び仮想環境に入って、cdで現在の階層まで戻る

   Windowsのactivateコマンド

   ```
   Set-ExecutionPolicy RemoteSigned -Scope Process
   ```

   実行ポリシーを聞かれたら、「Y」を入力してEnter

   ```
   Scripts\activate
   ```

   

#### アプリの指定

1. インストールしたアプリの指定

settings.py　INSTALLED_APPS 部分

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todo',
]
```

#### テンプレートの指定

1. TODOPROJECTフォルダ直下にtemplatesフォルダを作成
2. settings.py　TEMPLATES部分の'DIRS'の値を変更

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

#### データベースの設定

DATABASESの設定は、今回はSQLite3を使用するので変更の必要はない

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

#### 言語とタイムゾーン

言語とタイムゾーンを変更

```
LANGUAGE_CODE = 'ja'
 
TIME_ZONE = 'Asia/Tokyo'
```

#### staticフォルダ作成

1. cssや画像などを保存するために、static という名前のフォルダをTODOPROJECTフォルダ内に作成
2. settings.pyの最後の`STATIC_URL = '/static/'` の次に下記記述

VS-Codeで編集

settings.py

```
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```



### 現在のフォルダの状態

```
.
├── manage.py
├── static
├── templates
├── todo
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
└── todoproject
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-38.pyc
    │   └── settings.cpython-38.pyc
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## staticフォルダの準備

staticフォルダにcssやjavascript、画像などの準備をします。

今回はstatic.zipを展開してその内容を全てstaticフォルダに置きます。

static.zip

https://www.startlab-classroom.com/5/static.zip

### ルーティング　urls.pyの編集

#### プロジェクトのurls.pyを編集

VS-Codeで編集

1. todoproject/urls.pyの編集
   1. `path('', include('todo.urls')),` を追加
   2. from import文にincludeの追加

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
]
```

#### アプリのurls.pyを編集

VS-Codeで編集

1. todoフォルダに `urls.py` を新規作成（アプリのurls.pyは自動で作成されないので注意）
2. todo/urls.pyに以下コードを追加

```
from django.urls import path
from .views import todo

urlpatterns = [
    path('test/', todo)
]
```

### views.pyの編集

VS-Codeで編集

関数ベースビューを `views.py` に作成（Hello!と表示するためのもの）

1. `from django.http import HttpResponse`を追加
2. todo関数の定義　以下コード

```
from django.shortcuts import render
from django.http import HttpResponse

def todo(request):
	return HttpResponse('Hello!')
```

### サーバーの稼働

runserverを稼働させます。

ターミナルまたはパワーシェルで次の操作

```
python manage.py runserver
```

URLアドレスは以下を入れる。

http://127.0.0.1:8000/test/

画面に「Hello!」と表示されます。

### サーバーを停止

ctrl + c キーでサーバーを停止

### Gitブランチ作成

ここまでの内容を新しいブランチにします。ブランチ名は「no1_todo」とします。

Gitコマンドは以下

ターミナルまたはパワーシェルで次の操作

```
git add .
```

```
git commit
```

```
git checkout -b no1_todo
```

```
git checkout master
```

### GitHubにpush

GitHubに新しくリポジトリを作成します。

今回はmainではなくmasterでpushします。

```
git remote add origin https://github.com/[アカウント名]/dj_todo.git
```

```
git push -u origin master
```



## データベースの設定

### models.pyの編集

VS-Codeで作業

1. `models.py` の `class` を活用してテーブルを作成します。
   以下コードで、from import文以外のコードを貼り付ける

```
from django.db import models
 
 
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    duedate = models.DateField()
 
    def __str__(self):
        return self.title
```



#### makemigrationsとmigrateコマンドの実行

ターミナルまたはパワーシェルで次の操作

1. makemigrationsコマンド

```
python manage.py makemigrations
```

2. migrateコマンド

```
python manage.py migrate
```

OKがたくさん出たら完了

### スーパーユーザー作成

ターミナルまたはパワーシェルで次の操作

1. superuserの作成は次のコマンド

```
python manage.py createsuperuser
```

2. superuserの名前を聞いてきますので名前を入力します。（忘れないように！）
3. メールアドレスは不要。そのままEnter　
4. パスワードは好みのパスワードを指定します。（忘れないように！）
Superuser created successfully.と出ればOK



VS-Codeに戻って、admin.pyを次のように編集

```
from django.contrib import admin
from .models import TodoModel


admin.site.register(TodoModel)
```

これでデータ入力が可能になります。

### サーバーの稼働

ターミナルまたはパワーシェルで次の操作

runserverを稼働させて、admin画面に入りエラーが出ないか確認します。

```
python manage.py runserver
```

URLアドレスは以下を入れる。

http://127.0.0.1:8000/test/

画面に「Hello!」と表示されます。

### データ登録

次に、adminのアドレスを入れてデータを登録してみます。

http://127.0.0.1:8000/admin/

**http://127.0.0.1:8000ではないので注意！**

#### 認証

superuserで作成したユーザーとパスワードで認証します。

#### データ入力

1. 無事にadmin画面に入れたら、TODOの「追加」からいくつか予定を入力して確認します。

特にエラーが出なければ、データベースとの連携は取れています。

### サーバーを停止

ctrl + c キーでサーバーを停止

Windowsの場合も ctrl + c で停止します。



### Gitブランチ作成

ここまでの内容を新しいブランチにします。ブランチ名は「no2_todo」とします。

Gitコマンドは以下

```
git add .
```

```
git commit
```

```
git checkout -b no2_todo
```

```
git checkout master
```

### GitHubにpush

masterと作成したブランチをpushします。

```
git push origin --all
```



















# Herokuへデプロイ（PostgreSQL）

本番のサーバー環境にデプロイする場合、ローカル環境で構築した内容をsettings.py中心に各所の変更が必要になります。そうするとローカル環境での確認ができなくなります。

つまり、ローカル用の記述と本番用の記述が最低必要になります。この切り替えをシステマティックに行いたいものです。もっとも手軽な方法はGitのブランチを切り替える方法です。今回はGitのブランチをローカル用と本番用2つ追加していきます。`master`ブランチにHEROKUデプロイ用の設定を作成します。



現在のブランチを確認するgitコマンド

```
git branch
```

`master` ブランチに戻るgitコマンド

```
git checkout master
```



今後の処理はmasterブランチで行います。

## Herokuにデプロイ

### Herokuのデプロイに必要なパッケージ導入

1. TODOPROJECTフォルダにcdで移動して、次のコマンドを実行

2. dj-database-urlのインストール(今回は不要)

```
pip install dj-database-url gunicorn whitenoise
```

3. psycopgのインストール（今回は不要）

   **Macではエラーになるので注意**

```
pip install psycopg2
```

4. **MACでpsycopg2のインストールでエラーが出た場合**（今回は不要）
   psycopg2-binaryのインストール

```
pip install psycopg2-binary
```



## `requirements.txt`ファイル作成

1. TODOPROJECTフォルダ直下に、`requirements.txt`ファイルを作成しますが、以下のコマンドで作成することができます。

```
pip freeze > requirements.txt
```

2. 実行後出来た `requirements.txt` の内容の例
   今回はこれを使います。

```
asgiref==3.2.10
dj-database-url==0.5.0
Django==3.1.1
gunicorn==20.0.4
psycopg2-binary==2.8.6
pytz==2020.1
sqlparse==0.3.1
whitenoise==5.2.0
```

## Procfile

1. テキストエディタで`TODOPROJECT`ディレクトリ下に`Procfile`というファイルを作成

2. 次の行を記述します。`Procfile`に拡張子はありません。

Procfile記述内容

```
web: gunicorn todoproject.wsgi --log-file -
```



## `runtime.txt`ファイル

1. アプリを作成したPCのPythonのバージョンを確認

   ```
   python -V
   ```

2. テキストエディタで``TODOPROJECT``ディレクトリ下に`runtime.txt`というファイルを作成して、Pythonのバージョンを次のテキストを例に書き込む。

```
python-3.9.0
```

## settings.pyの編集

#### ALLOWED_HOSTの変更

1. settings.py ALLOWD_HOSTの編集

```
ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']
```

2. DEBUG は`DEBUG = False`に変更

3. MIDDLEWARE の2行目に ` 'whitenoise.middleware.WhiteNoiseMiddleware',`を追加

4. INSTALLED_APPS に`'gunicorn'` 追加

5. Postgre SQLに対応するためにすることは次のDATABASEの記述を変更するだけです。

   DATABASEは`DATABASES = {'default': dj_database_url.config()}`に変更

8. 最終行は以下になるように追加

```
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
```

9. 最初にimportも追加

```
import dj_database_url
```

HerokuLに対応したsettings.py全てコードは以下


settings.py 

```python
import dj_database_url
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY_TODO')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todo',
    'gunicorn',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'todoproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'todoproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {'default': dj_database_url.config()}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

```

--------------------------------------------------------               以下説明                      --------------------------------------------------------

settings.pyの次の内容はローカルサーバーにstaticの場所を教えています。

```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```

次の内容は本番サーバーにstaticの場所を教えます。

`staticfiles`を指定して`python manage.py collectstatic`を実行すると新規にstaticfilesフォルダを作成してその中に静的なファイルを集めます。本番サーバーにはstaticフォルダではなく、staticfilesをデプロイします。

```
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

--------------------------------------------------------          ここまで説明                   --------------------------------------------------------

## wsgi.pyの編集

wsgi.pyの編集

```python
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todoproject.settings')

application = get_wsgi_application()
```

### collectstaticの実行

全てのアプリケーションにある静的ファイルを自動で一箇所に集めてくれます。

```
python manage.py collectstatic
```

### gitコマンド実行

```
git add .
```

```
git commit
```



## Herokuアカウント

### Heroku CLIをインストール

1. MAC の場合
   Home brewでインストールします。

   HomebrewはMACのパッケージマネージャーです。
   
   これをインストールしておけばPythonも複数のバージョンをインストールできるようになります。

   
   

まずはHome brewをインストールします。

   https://brew.sh/index_ja

Homebrewのページからインストールのところに表示されているコードをターミナルで実行します。

```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

   Homebrewがインストールされたら以下コマンドでHeroku CLIをインストールします。

   ```
   brew install heroku/brew/heroku
   ```

   

2. Windowsの場合
   次のURLのページからWindows用のインストーラーをダウンロードしてインストールします。
   インストーラーのチェックはそのままチェックが入った状態でNextボタンで進みインストールします。

   https://devcenter.heroku.com/articles/heroku-cli

ここでパワーシェルまたはターミナルを再起動

### Herokuにログイン

1. 次にこのコマンドを実行して、自分のコンピュータでHerokuアカウントを認証します。

```
heroku login
```

2. heroku: Press any key to open up the browser to login or q to exit: 
   と表示されるので何かキーを押すとHerokuのページが立ち上がりますので認証します。



## Webアプリケーション名をつける

1. 名前を考えたら次のコマンドを実行します。

```
heroku create todo-lesson
```

2. HEROKUに名前を任せる場合は次のコマンド

```
heroku create
```

 

## Herokuにデプロイ準備

1. ログインしたHEROKUページから該当アプリを選択
2. ダッシュボードのsettingタブを選択
3. Config Varsを選択
4. キーに　`DISABLE_COLLECTSTATIC`  をセット
5. 値に `1` をセット
6. Addボタンをクリック

## PostgreSQLの準備

1. Herokuのダッシュボードに入ります。
2. グローバルナビの「Overview」を選択します。
3. 「Installed add-ons」が左側にあります。
4. 「Installed add-ons」のConfigure Add-onsを選択します。
5. Add-onsのサーチボックスにPostgresと入力すると「Heroku Postgres」が表示されるので選択します。
6. 出てきたBoxでplan nameがにHobby Dev となってFreeとなっていることを確認します。
7. Submit Order Formをクリック
8. グローバルナビの「Setting」を確認します。
9. Config Varsのところにある「Reveal Config Vars」をクリックします。
10. DATABASE_URLにPostgreSQLの情報が入っていることを確認します。

#### DATABASE_URLの見方

DATABASE_URLに入っている値がデータベースの設定情報になります。

```
postgres://ユーザ名:パスワード@ホスト名:5432/データベース名
```

実例は次のようになります。（*は実際は半角英数記号など）

```
postgres://wclj***********:00e***********************************************************@ec2-*********************.amazonaws.com:5432/d2h*********lsl
```

この情報をsettins,pyで指定したDATABASESのdj_database_url.config()が読み取ってくれる仕組みです。

```
DATABASES = {'default': dj_database_url.config()}
```

### SECRET_KEYの設定

HerokuのダッシュボードのsettingでConfig Varsを選択してSECRET_KEYの設定を行います。

1. KEYに`SECRET_KEY_TODO`と記述
2. VALUEにシークレットキーの値を貼り付けます。値はクオートで囲みます。

## Herokuへデプロイ

デプロイにはGitのpushを使います。

1. `heroku create` コマンドを実行したときに、あなたのリポジトリにHerokuのリモートサーバーが自動的に追加されています。

2. 次のコマンドを実行してpushする先をgitに登録

```
heroku git:remote -a アプリ名
```

3. Herokuにデプロイコマンド
   **Pushする前にaddとcommitやらないとダメ！**

```
git push heroku master
```

現在、自分がチェックアウトして作業しているブランチがmaster以外で、たとえばmainブランチで作業している場合は、次のコマンドをいれる。

```
pushを実行するコマンド
git push heroku main:master
```

以下のエラーが出た場合、ネットの環境の問題があるかもしれません。

授業終了後に再度試してください。

```
fatal: failed to read object 857180863aa54867afc63211abf7fb25b134a600: Interrupted system call
fatal: the remote end hung up unexpectedly
fatal: the remote end hung up unexpectedly
fatal: the remote end hung up unexpectedly
error: failed to push some refs to 'https://git.heroku.com/todo-lesson2.git'
```

一度の転送量を増やす設定にすると解決するかもしれません。

```
git config http.postBuffer 10485760
```

### Heroku上でmigrateが必要

1. データベースの設定が終了したら、migrateします。

```
heroku run python manage.py migrate
```

### superuserの作成

1. superuserは次のコマンドです。

```
heroku run python manage.py createsuperuser
```

名前、パスワードを事前に準備しておきましょう。メールアドレスは何も入力せずに通ります。

