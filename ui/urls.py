from . import views
from django.urls import path

urlpatterns = [
    path('', views.ui, name='ui'),
    path('post/', views.post, name='post'),
    path('feed/<int:postId>', views.feed, name='feed'),
    path('postMessage/', views.postMessage, name='postMessage'),
    path('profile/<int:UserId>', views.accountPage, name='accountPage'),
    path('dm/', views.dm, name='dm'),
    path('friends/', views.friends, name='friends'),
]
