# flud/mysql/Dockerfile

FROM mysql/mysql-server:5.7

ENV MYSQL_ROOT_PASSWORD=xyz \
    MYSQL_DATABASE=crud \
    MYSQL_USER=foo \
    MYSQL_PASSWORD=xyz

COPY db_init.sql /docker-entrypoint-initdb.d

EXPOSE 3306