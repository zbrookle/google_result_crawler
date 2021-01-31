FROM postgres

RUN apt-get update && apt-get install -y python3 python3-pip

RUN /usr/bin/pip3 install kazoo \
    click

COPY storage/result_database_setup.sh /docker-entrypoint-initdb.d/init-user-db.sh

COPY join_party.py join_party.py