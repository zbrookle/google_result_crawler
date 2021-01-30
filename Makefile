start:
	docker build reverse_proxy/ -t testing-proxy
	docker build workers/ -t celery-worker
	docker stack deploy -c docker-compose.yaml celery-test
stop:
	docker stack rm celery-test
logs: 
	docker service logs celery-test_test
get:
	python workers/project/zookeeper/get_children.py