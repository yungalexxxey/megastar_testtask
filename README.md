# Задание

> Реализовать на Питоне сервис, который хранит в PostgreSQL данные о писателях и их книгах, и умеет по HTTP-запросу GET /writers/<writer_id>  возвращать информацию о писателе и его книгах в следующем формате (JSON):



&emsp;Любые изменения в проекте необходимо вносить в .env файл. Там можно изменить: название базы данных, пользователя,
пароль, хост и порт ( как PostgreSQL, так и FastAPI)

&emsp;Для запуска проекта нужно прописать следующие команды в терминале:

- git clone https://github.com/yungalexxxey/megastar_testtask.git
- pipenv install -r req.txt
- pipenv shell
- docker-compose build
- docker-compose up -d
- python3 main.py init (если необходимо запустить сервис с готовой БД и тестовыми данными)
- python3 main.py (если необходимо запустить сервис с чистой БД)

&emsp;Пример запроса из терминала:
>  curl -X 'GET' \\
  'http://0.0.0.0:8000/writers/1' \\
  -H 'accept: application/json' 

&emsp;Где 0.0.0.0 - HOST, прописанный в .env файле, а 8000 - PORT.