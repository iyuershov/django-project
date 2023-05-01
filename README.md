# Итоговый проект. Веб-разработка на Python и Django
### Ершов Иван Юрьевич МИВТ-21-3-16


## Запуск приложения
### Перед началом работы
При prod-deployment сменить пароль от superuser в 13 строке Dockerfile
### Инициализация образа и запуск контейнера
Запуск миграционных тестов встроен в Dockerfile. 
Соответственно, если в тестах будет ошибка, 
то build не отработает и образ не будет создан/обновлен.
```
> docker build -t ershov-django-project .
> docker run --rm -it -d -p 8888:8888 ershov-django-project
```
Проверяем, что все отработало корректно http://localhost:8888/admin

Если пароль не был изменен, то стандартные параметры входа в админку следующие:
```
User: admin
Pass: Place-Supersecret-Passw0rd-Here
```

Проверяем, что в сущностях Albums и Photos 
создано по 2 объекта объявленных в `albums_api/fixtures/initial_data.json`.