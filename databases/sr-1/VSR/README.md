###mongodb_task

Для развертывания mongodb с помощью docker были использованы следующие команды:
<pre>
docker network create some-network
docker run --name some-mongo --network some-network -d mongo
docker run -it --network some-network --rm mongo mongosh --host some-mongo test
</pre>

Сначала создаём новую сеть, после развертываем саму mongodb под именем some-mongo и связываем её с созданой сетью
<br/>
Последняя же команда запускает локальный сервер с mongodb, где уже мы и сможем работать с БД.
<br/>
Команды с демонстрацией простых возможностей продемонстрированы на скриншотах mongo_admin и mongo_proof. (Создание admin пользователя, коллекции user, а также простых действий с этой коллекцией)
