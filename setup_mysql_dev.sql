-- Prepares a MySQL server for the project:
    -- Create database hbnb_dev_db
    -- Create new user hbnb_dev with password hbnb_dev_pwd in localhost
    -- Grants all privileges for hbnb_dev on hbnb_dev_db
    -- Grants SELECT privilege for hbnb_dev on performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;