-- Creates database environment dev testing

CREATE DATABASE IF NOT EXISTS xlease_dev_db;
CREATE USER IF NOT EXISTS 'xlease_dev'@'localhost' IDENTIFIED BY 'xlease_dev_pwd';
GRANT ALL PRIVILEGES ON `xlease_dev_db`.* TO 'xlease_dev'@'localhost';
FLUSH PRIVILEGES;
