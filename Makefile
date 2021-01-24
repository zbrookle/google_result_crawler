start:
	docker-compose build
	docker-compose up --scale requester=3