from django.apps import AppConfig


class HomeworkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Homework'

    def ready(self):
        import Homework.signals
