start:
	docker build -f ./storage/Dockerfile . -t postgres-shard
	docker build reverse_proxy/ -t testing-proxy
	docker build -f ./workers/Dockerfile . -t celery-worker
	docker stack deploy -c docker-compose.yaml celery-test
stop:
	docker stack rm celery-test
logs: 
	docker service logs celery-test_result-shard
get:
	python workers/project/zookeeper/get_children.py
dozzle:
	docker run --name dozzle -d --volume=/var/run/docker.sock:/var/run/docker.sock -p 8888:8080 amir20/dozzle:latest