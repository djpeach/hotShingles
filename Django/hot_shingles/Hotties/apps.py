from django.apps import AppConfig


class HottiesConfig(AppConfig):
    name = 'Hotties'

    def ready(self):
        import Hotties.signals
