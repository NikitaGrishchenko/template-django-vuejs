# DJANGO & VUE TEMPLATE

```
make install – установка всех зависимостей
make run – запуск серверов
make createadmin – создание админа
make migrate – миграции

python3 -m venv .venv – создание виртуального окружения Linux
source .venv/bin/activate – активация виртуального окружения Linux

python -m venv .venv – создание виртуального окружения Windows
source .venv/Scripts/activate – активация виртуального окружения Windows

pip freeze – вывести установленные модули в консоль
pip freeze > requirements.txt – сохранить установленные модули в файл

pip install -r requirements.txt – установка зависимостей из requirements.txt
yarn – установк зависимостей для frontend

yarn serve – старт сервера Vue
python ./backend/manage.py runserver – старт сервера Django

python ./backend/manage.py makemigrations – применить миграции
python ./backend/manage.py migrate – выполнить миграции

Создание приложения example
1. создать папку example в backend/apps
2. cd backend
3. django-admin startapp example apps/example
```
# TASK
```
[ ] Пакетный менеджер pipenv
[ ] Написать скрипт для создания приложений в папке apps
[ ] Настроить dev server в vue config для обновления при сохранении
[ ] Добавить пути для media и статики
[ ] Подключить шрифт Roboto
[ ] TIME_ZONE = "Europe/Moscow"
```
