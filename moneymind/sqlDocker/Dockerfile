FROM mariadb:latest
LABEL maintainer="Thomas Palma"
COPY . /docker-entrypoint-initdb.d

RUN chown -R mysql:mysql /var/lib/mysql