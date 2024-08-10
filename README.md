# Практика НПЦ-КСБ

Система учета студентов на DRF и Vue.js 3

Используется Docker Compose для запуска нескольких образов, а также Celery + Redis для задачи автоинкремента курса студентов.

## Скриншоты

| ![image1](https://github.com/user-attachments/assets/6dd81260-7eea-4cb3-b27d-a751cccb52aa "Страница авторизации") | ![image2](https://github.com/user-attachments/assets/e350aa7c-25eb-4347-8c25-c7c0d4320da9 "Раздел студентов (в виде карточек)") |
|:---:|:---:|
| ![image3](https://github.com/user-attachments/assets/a8d1e11e-9325-452e-a3ea-9265a6a94deb "Раздел наставников (в виде карточек)") | ![image4](https://github.com/user-attachments/assets/fe25ca51-30b9-4561-8591-55c7e608e884 "Просмотр анкеты") |
| ![image5](https://github.com/user-attachments/assets/f503fb4f-25ff-40b1-828d-9095c47d84b2 "Изменение анкеты") | ![image6](https://github.com/user-attachments/assets/d4655329-4278-49c9-8a58-05f6bdddce53 "Раздел стажировок и практик") |
| ![image7](https://github.com/user-attachments/assets/2a697b1d-2b53-41df-94df-05dc7995fc74 "Раздел работы с применением фильтрации и поиска") | ![image8](https://github.com/user-attachments/assets/eeacf330-f20a-4d1b-93ed-4e6dc0da60bf "Автоинкремент курса (выполнение в celery worker)") |

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
