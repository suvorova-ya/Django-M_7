from django.apps import AppConfig



class InternetShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'internet_shop'
    # # нам надо переопределить метод ready, чтобы при готовности нашего приложения импортировался модуль со всеми функциями обработчиками
    # def ready(self):
    #     import internet_shop.signals
