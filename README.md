"DJANGO + VUE"

python3 -m venv venv - создание виртуального окружения
source venv/bin/activate - активация виртуального окружения

Чтобы посмотреть установленные модули для данного проекта, пишите : pip freeze Чтобы сохранить их в файл, то: pip freeze > requirements.txt А для того, чтобы установить всенеобходимые зависимости для уже готового проекта, нужно набрать pip install -r requirements.txt , при этом файл должен находится в корне, т.е. там же, где и manage.py

python ./backend/manage.py runserver - старт сервера
python ./backend/manage.py migrate - выполнить миграции
