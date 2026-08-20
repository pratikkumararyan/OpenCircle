from . import views
from django.urls import path
from django.conf.urls import static
from django.conf import settings

urlpatterns = [
    path('', views.ui, name='ui'),
    path('post/', views.post, name='post'),
    path('dm/', views.dm, name='dm'),
    path('friends/', views.friends, name='friends'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
