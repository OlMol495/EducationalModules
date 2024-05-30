Проект "Образовательные модули"
Проект управляется админом и модераторами. Каждый образовательный модуль состоит из серии обучающих видео, доступ к которым имеют только авторизованные пользователи.
Обучающие видео должны быть с youtube.
Направление
Backend.

Особенности
Сервис реализован на фреймворке Django 5.0.
Проект использует djangorestframework.
Для наследования сущности пользователь, используется модель AbstractUser.
Настроен CORS.
Используется Swagger.
Проект "завёрнут" в Docker.
Фикстуры для заполнения базы данных находятся в файлах userdata.json и educationdata.json, загрузить командой:
python manage.py dumpdata > filename.json
B Windows: python -Xutf8 manage.py dumpdata > filename.json

Алгоритм запуска сервиса
Если не использовать Docker

Клонируйте содержимое данного репозитория: git clone https://github.com/OlMol495/EducationalModules.git

создайте файл .env в корне проекта и добавьте свои данные по образцу из env.sample.

Установите зависимости в venv: pip3 install -r requirements.txt.

Создайте базу данных, например, через консоль:

psql -U postgres                                                                                                                    
create database project_name;
q\                                                                                               
Сделайте миграции: 
                    python manage.py makemigrations

                   python manage.py migrate.

Запустите проект: python manage.py runserver

Создайте суперюзера использую команду: python manage.py csu

Откройте браузер и перейдите по адресу http://127.0.0.1:8000 для доступа к приложению.

Документация для API реализована с помощью drf-yasg и находится на следующих эндпоинтах:

http://127.0.0.1:8000/redoc/
http://127.0.0.1:8000/swagger/
Тестирование проекта
Для тестирования проекта запустить команду: python manage.py test

Запуск проекта с помощью Docker Compose
Для запуска проекта с помощью Docker Compose выполните следующие шаги:

Установите Docker и Docker Compose, если они еще не установлены на вашем компьютере.

Сборка образов
docker-compose build

Запуск контейнеров
docker-compose up

Запуск контейнеров в фоне
docker-compose up -d

Сборка образа и запуск в фоне после успешной сборки
docker-compose up -d —build

Выполнение команды внутри контейнера
docker-compose exec <app> <command>

Откройте браузер и перейдите по адресу 0.0.0.0:8000 для доступа к проекту.

Остановить работу docker-compose можно командой docker-compose stop в терминале
