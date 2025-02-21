# term4

<h2>Задание 1</h2>
<ul>
  <li>Раздел "Instance" - предоставляет пользователям возможность настраивать параметры соединения, конфигурацию сервера, управление пользователями и другие аспекты работы с базами данных.
    <ul>
      <li>Позволяет настроить метод подключения к серверу (Например, самый простой вариант это указать адрес сервера, порт, имя пользователя и пароль для доступа к базе данных).</li>
      <li>Позволяет управлять пользователями и удаленным доступом.</li>
      <li>Позволяет настраивать сервер или использовать файл конфигурации для него.</li>
      <li>Содержит серверный логгер.</li>
    </ul>
  </li>
<br/>
  <li>Раздел "Perfomance" - предназначен для мониторинга и анализа производительности базы данных, а также для оптимизации работы SQL-серверов MySQL.
    <ul>
      <li>Предоставляет инструменты для мониторинга производительности. (Отображает использование CPU, памяти и сетевых ресурсов и т.п., а также информацию о активности серверов, включая информацию о текущих подключениях, запросах и покое).</li>
      <li>Даёт возможность анализа выполнения конкретных запросов, что позволяет выявить длинные или частые запросы, которые могут замедлять работу системы.</li>
      <li>Возможность изменения конфигурации сервера для улучшения его производительности, включая настройки буферов, кэшей и других параметров. (Пунтк Perfomance Schema setup)</li>
      <li>Предоставляет огромное количество инструментов для сбора статистики, связанной с затратами ресурсов на конкретные заадчи.</li>
    </ul>
  </li>
</ul>
<br/>
<h2>Задания 2 и 3</h2>
Запрос для создания таблицы из задания 2:
<pre>
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
</pre>
<br/>
<h2>Заданиe 4</h2>
<pre>
INSERT INTO `simpledb`.`users` (`id`, `name`, `email`) VALUES ('1', 'Danil', 'vayzera@yandex.ru');
INSERT INTO `simpledb`.`users` (`id`, `name`, `email`) VALUES ('2', 'Timofei', 'kirillov-timko@rumbler.ru');
INSERT INTO `simpledb`.`users` (`id`, `name`, `email`) VALUES ('3', 'Artemii', 'karandashov.artemij@yandex.ru');
INSERT INTO `simpledb`.`users` (`id`, `name`, `email`) VALUES ('4', 'Dima', 'dimadima@mail.ru');
</pre>
<br/>
<h2>Заданиe 5</h2>
<pre>
ALTER TABLE `simpledb`.`users` 
ADD COLUMN `gender` ENUM('M', 'F') NULL AFTER `email`,
ADD COLUMN `bday` DATE NULL AFTER `gender`,
ADD COLUMN `postal_code` VARCHAR(10) NULL AFTER `bday`,
ADD COLUMN `rating` FLOAT NOT NULL AFTER `postal_code`,
ADD COLUMN `created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP AFTER `rating`;
</pre>
<br/>
<h2>Заданиe 5</h2>
TIMESTAMP CURRENT_TIMESTAMP() Позволяет автоматически добавлять время создания записи в БД с точностью до секунд.
<pre>
ALTER TABLE `simpledb`.`users` 
ADD COLUMN `gender` ENUM('M', 'F') NULL AFTER `email`,
ADD COLUMN `bday` DATE NULL AFTER `gender`,
ADD COLUMN `postal_code` VARCHAR(10) NULL AFTER `bday`,
ADD COLUMN `rating` FLOAT NOT NULL AFTER `postal_code`,
ADD COLUMN `created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP AFTER `rating`;
</pre>
<br/>
<h2>Заданиe 5</h2>
TIMESTAMP CURRENT_TIMESTAMP() Позволяет автоматически добавлять время создания записи в БД с точностью до секунд. <br/>
Столбцы postal_code и bday предоставляют личную информацию, которой пользователь возможно не захочет делиться,а значит они могут бытьь NULL 
<pre>
ALTER TABLE `simpledb`.`users` 
ADD COLUMN `gender` ENUM('M', 'F') NULL AFTER `email`,
ADD COLUMN `bday` DATE NULL AFTER `gender`,
ADD COLUMN `postal_code` VARCHAR(10) NULL AFTER `bday`,
ADD COLUMN `rating` FLOAT NOT NULL AFTER `postal_code`,
ADD COLUMN `created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP AFTER `rating`;
</pre>
<h2>Задания 6 и 7</h2>
<pre>
ALTER TABLE `simpledb`.`users` 
INSERT INTO `simpledb`.`users` (`name`, `email`, `postal_code`, `gender`, `bday`,
`rating`) VALUES ('Ekaterina', 'ekaterina.petrova@outlook.com', '145789', 'f',
'2000-02-11', '1.123');
INSERT INTO `simpledb`.`users` (`name`, `email`, `postal_code`, `gender`, `bday`,
`rating`) VALUES ('Paul', 'paul@superpochta.ru', '123789', 'm', '1998-08-12', '1');
</pre>
<pre>
UPDATE `simpledb`.`users` SET `bday` = '2004-09-30' WHERE (`id` = '1');
UPDATE `simpledb`.`users` SET `bday` = '2004-10-09' WHERE (`id` = '2');
UPDATE `simpledb`.`users` SET `bday` = '2005-12-24' WHERE (`id` = '3');
UPDATE `simpledb`.`users` SET `bday` = '2004-01-4' WHERE (`id` = '4');
</pre>
<h2>Заданиe 8</h2>
При удалении связанных записей они пропадают из обоих таблиц.
<pre>
CREATE TABLE `simpledb`.`resume` (
  `resumeid` INT NOT NULL AUTO_INCREMENT,
  `userid` INT NOT NULL,
  `title` VARCHAR(100) NOT NULL,
  `skills` TEXT NULL,
  `created` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP(),
  PRIMARY KEY (`resumeid`));
ALTER TABLE `simpledb`.`resume` 
ADD CONSTRAINT `userid`
  FOREIGN KEY (`userid`)
  REFERENCES `simpledb`.`users` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;
</pre>
<h2>Заданиe 9</h2>
Запросы на добавление новых резюме
<pre>
INSERT INTO `simpledb`.`resume` (`resumeid`, `userid`, `title`, `skills`) VALUES ('1', '2', 'Timofei\'s resume', 'wiring, networks and telecommunications');
INSERT INTO `simpledb`.`resume` (`resumeid`, `userid`, `title`, `skills`) VALUES ('2', '1', 'Danil\'s resume', 'managment');
</pre>
При попытке добавление резюме с несуществующим userid выводиться ошибка (Скриншот Error_1)
<pre>
INSERT INTO `simpledb`.`resume` (`resumeid`, `userid`, `title`, `skills`, `created`) VALUES ('3', '7', 'WhoKnows', 'AllYouNeed', '');
</pre>
Количество резюме для одного пользователя ничем не ограничевается т.к. ни одно из полей не имеет тэга Unique (UQ), а значит userid могут повторяться.
<h2>Заданиe 10</h2>
Удаление записи из таблицы users удаляет и соответствующее резюме из resume
<pre>
DELETE FROM `simpledb`.`users` WHERE (`id` = '1');
</pre>
При обнавлении userid в таблице users оно автоматически обнавляется и в таблице resume (Скриншоты old_id и new_id)
<pre>
UPDATE `simpledb`.`users` SET `id` = '1' WHERE (`id` = '2');
</pre>
