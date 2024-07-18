from django.apps import AppConfig


class EmailseviceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "emailservice"

    def ready(self):
        from . import signals
