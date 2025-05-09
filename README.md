#
Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.
#
Ключевые возможности сервиса:
* генерация коротких ссылок и связь их с исходными длинными ссылками,
* переадресация на исходный адрес при обращении к коротким ссылкам.
#
Технологии
* Python
* Flask
* Jinja2
* SQLAlchemy

#
Пользовательский вариант короткой ссылки не должен превышать 16 символов.

API проекта доступен всем желающим. Сервис обслуживает только два эндпоинта:
* /api/id/ — POST-запрос на создание новой короткой ссылки;
* /api/id/<short_id>/ — GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору.

#
Для запуска:

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

* Если у вас Linux/macOS

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

```
pip install -r requirements.txt
```
Создать и заполнить файл .env:
```
FLASK_APP=yacut
FLASK_ENV=development
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=YOUR_SECRET_KEY
```
Автор: Дзюба А.А.
