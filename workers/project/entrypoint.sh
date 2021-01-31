nohup python join_party.py "/celery/workers" $TASK_NAME &
celery -A project.application worker -n "${TASK_NAME}@%h" --loglevel=DEBUG