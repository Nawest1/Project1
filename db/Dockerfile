
FROM mysql:5.7

ENV MYSQL_ROOT_PASSWORD=password123
ENV MYSQL_DATABASE=flask-db
WORKDIR /db
COPY CreateTable.sql /docker-entrypoint-initdb.d/
