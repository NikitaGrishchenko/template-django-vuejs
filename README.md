"DJANGO + VUE"

python3 -m venv venv – создание виртуального окружения
source venv/bin/activate – активация виртуального окружения Linux
venv\Scripts\activate – активация виртуального окружения Windows
pip install -r requirements.txt – установка зависимостей из requirements.txt

django-admin startproject backend – создание backend на django

Чтобы посмотреть установленные модули для данного проекта, пишите : pip freeze Чтобы сохранить их в файл, то: pip freeze > requirements.txt А для того, чтобы установить всенеобходимые зависимости для уже готового проекта, нужно набрать pip install -r requirements.txt , при этом файл должен находится в корне, т.е. там же, где и manage.py

yarn install - установк зависимостей для frontend
yarn serve – старт сервера vue.js

python ./backend/manage.py runserver – старт сервера ###
python ./backend/manage.py migrate – выполнить миграции ###
