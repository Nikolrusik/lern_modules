# How to run

В данном проекте открытое API с которым можно работать без авторизации

## Step 1

Для начала создайте папку для проекта и выполните команду:

```
git clone https://github.com/Nikolrusik/lern_modules.git /yourfolder
```

## Step 2

Откройте проект в терминале и создайте виртуальное окружение:

```
cd yourfolde
python3 -m venv venv
```

## Step 3

Активируйте окружение и установите зависимости:

```
source './venv/bin/activate'
pip install requirements.txt
```

## Step 4

Выполните следующие команды, чтобы у вас запустился сервер:

```
python3 manage.py runserver
```

## Step 6

Перейдите на http://127.0.0.1:8000/api/lern_module/ чтобы увидеть интерфейс API
Перейдите на http://127.0.0.1:8000/api/doc/ чтобы увидеть документацию по проекту

## Step 7

Выполните следующую команду, чтобы выполнить тесты

```
python3 manage.py test
```

**Done!**
