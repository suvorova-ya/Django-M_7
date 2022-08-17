from django.urls import path
from. import views
from .views import subscribe_user

urlpatterns = [
    path('',views.news.as_view(),name = "news"),
    path('create',views.PostCreateView.as_view(), name='news_create'),  # Ссылка на создание новости
    path('<int:pk>',views.NewsDetail.as_view(),name = 'details_view'), # Ссылка на чтение новости
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='news_create'),  # Ссылка на обновление новости
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='news_delete'),  # Ссылка на удаление новости
    path('post-like/<int:pk>', views.PostLike, name="post_like"),
    path('subscribers/subscribe',subscribe_user, name='subscribe'), #подписка на категории
    path('subscribers/', views.Subscribers.as_view(), name='subscribers'), # Ссылка на просмотр категорий

    ]