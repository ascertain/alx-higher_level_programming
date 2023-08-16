-- 0x0E. SQL - More queries, task 1. Root user
-- Creates user `user_0d_1`, sets pwd, and grants all privileges.
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES 
ON *.*
TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;