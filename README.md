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
