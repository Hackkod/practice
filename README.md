# Практика НПЦ-КСБ

Ссылка на [figma](https://www.figma.com/design/Eo3Rwg6qCkBNRMTOOFX3Pa/Practice?node-id=0-1&t=ZH0QG2kp30Qajf8F-1) с диаграммами.

## Мануал по docker ;)

### Собрать docker контейнер через docker-compose:
```console
$ docker-compose up --build -d
```

### Удалить созданный docker контейнер:
```console
$ docker-compose down -v
```

### Остановить docker контейнер (без удаления):
```console
$ docker-compose stop
```

### Запустить docker контейнер:
```console
$ docker-compose start
```

### Перейти в консоль web контейнера:
```console
$ docker-compose exec web bash
```