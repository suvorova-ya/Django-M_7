from django.apps import AppConfig
import redis

class NewPortalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news_portal'

    def ready(self):
        import news_portal.signals
        import news_portal.apscheduler
        news_portal.apscheduler.run()

class ProfanityConfig(AppConfig):
    name = 'profanity'
