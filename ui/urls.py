from . import views
from django.urls import path

urlpatterns = [
    path('', views.ui, name='ui'),
    path('post/', views.post, name='post'),
    path('dm/', views.dm, name='dm'),
    path('friends/', views.friends, name='friends'),
]
