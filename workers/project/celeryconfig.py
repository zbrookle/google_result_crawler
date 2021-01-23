# Broker settings.
broker_url = "amqp://guest:guest@message-broker:5672//"

# Using the database to store task state and results.
result_backend = "db+postgresql://postgres:postgres@storage/celery_results"
