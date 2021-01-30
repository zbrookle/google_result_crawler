name=$1
python project/zookeeper/join_party.py $name
celery -A project.application worker -n "${name}@%h" --loglevel=DEBUG