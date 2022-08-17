from django.urls import path
from. import views
from .views import Products, AppointmentView

urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', Products.as_view()),
   path('make_appointment/', AppointmentView.as_view(), name='make_appointment'),
   # path('<int:pk>', ProductsDetail.as_view()),

]