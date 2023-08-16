-- lists all privileges of the MySQL users
-- user_0d_1 and user_0d_2

# Create user user_0d_1
echo "CREATE USER 'user_0d_1'@'localhost';" | mysql -hlocalhost -uroot -p

# Grant privileges to user_0d_1
echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" | mysql -hlocalhost -uroot -p

# Create user user_0d_2
echo "CREATE USER 'user_0d_2'@'localhost';" | mysql -hlocalhost -uroot -p

# Grant privileges to user_0d_2
echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';" | mysql -hlocalhost -uroot -p

# List privileges for user_0d_1
echo "SHOW GRANTS FOR 'user_0d_1'@'localhost';" | mysql -hlocalhost -uroot -p

# List privileges for user_0d_2
echo "SHOW GRANTS FOR 'user_0d_2'@'localhost';" | mysql -hlocalhost -uroot -p
