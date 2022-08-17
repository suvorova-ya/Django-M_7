from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news_portal.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('news/', include('news_portal.urls')),
    path('products/', include('internet_shop.urls')),
    # path('', include('protect.urls')),
    path('accounts/', include('allauth.urls')),
    path('account/', include('account.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



