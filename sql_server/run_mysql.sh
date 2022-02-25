#!/bin/bash

# after running containaer:
# docker exec -ti sql
# mysql -uroot -p
# insert data base queries

# mysql> CREATE USER 'monty'@'%' IDENTIFIED BY '123';
# mysql> GRANT ALL PRIVILEGES ON *.* TO 'monty'@'%'
#     ->     WITH GRANT OPTION;
# show processlist;

# show databases;
# create database testdb;
# create table testdb.login(username text, password char(60));
# insert into testdb.login values ("abc@gmail.com", "123");

# use testdb;
# show tables;
# select * from login;

#SQL_CONF=/etc/mysql/my.cnf
SQL_CONF=/home/idofar/login_project/mysql_conf/conf.d
SQL_DATA_DIR=/home/idofar/login_project/mysql_data

docker run \
--rm \
--detach \
--name=sql \
--env="MYSQL_ROOT_PASSWORD=123" \
--publish 3306:3306 \
--volume=${SQL_DATA_DIR}:/var/lib/mysql \
mysql/mysql-server:latest

#--volume=${SQL_CONF}:/etc/mysql/conf.d \
#--volume=${SQL_DATA_DIR}:/var/lib/mysql \
