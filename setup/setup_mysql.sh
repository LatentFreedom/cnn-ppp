#! /bin/bash

mysql -uroot -p -e "CREATE DATABASE ppp"
mysql -uroot -p ppp < ppp.sql
mysql -uroot -p -e "CREATE USER ppp_admin@localhost IDENTIFIED BY 'password';"
mysql -uroot -p -e "GRANT ALL PRIVILEGES ON ppp.* TO 'ppp_admin'@'localhost';"
mysql -uroot -p -e "FLUSH PRIVILEGES;"