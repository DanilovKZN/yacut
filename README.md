# Проект **YaCut**

## Коротко о проекте

Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.


## Как запустить проект:


Клонировать репозиторий и перейти в него в командной строке:


```

git clone

```

  

```

cd yacut

```

  

Cоздать и активировать виртуальное окружение:

  

```

python3 -m venv venv

```

  

* Если у вас Linux/MacOS

  

```

source venv/bin/activate

```

  

* Если у вас windows

  

```

source venv/scripts/activate

```

  

Установить зависимости из файла requirements.txt:

  

```

python3 -m pip install --upgrade pip

```
Отредактировать файл `.env`  
```
DB=sqlite:///db.sqlite3 (или другая)

FLASK_APP=yacut

FLASK_ENV=development (либо прод)

SECRET_KEY='Ваш ключ'
```

Применить миграции

```
flask db migrate -m "Суть миграции"
flask db upgrade

```

Запустить сервер

```
flask run

```


Технологии
```
Python
Flask
Flask-SQLAlchemy
Flask-WTF
Flask-Migrate
```
Автор
```
Данилов Николай
