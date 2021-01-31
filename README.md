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
[x] Пакетный менеджер poetry
[ ] Написать скрипт для создания приложений в папке apps
[x] Настроить dev server в vue config для обновления при сохранении
[x] Добавить пути для media и статики
[ ] Подключить шрифт Roboto
[x] TIME_ZONE = "Europe/Moscow"
[ ] добавить local setting и deploy setting
[ ] добавить БД в gitignore
```
