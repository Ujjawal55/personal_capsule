from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "home"

    def ready(self):  # NOTE: here you have to import the django signals for it work
        import home.signals
