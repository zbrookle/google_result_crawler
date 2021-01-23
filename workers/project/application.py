from celery import Celery

app = Celery("project", include=["project.tasks"],)
default_config = "project.celeryconfig"
app.config_from_object(default_config)

if __name__ == "__main__":
    app.start()
