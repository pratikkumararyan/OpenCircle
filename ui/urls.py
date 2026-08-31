from . import views
from django.urls import path

urlpatterns = [
    path('', views.ui, name='ui'),
    path('exit/', views.exit, name='exit'),
    path('feed/<int:postId>', views.feed, name='feed'),
    path('profileFeed/<int:postId>', views.profileFeed, name='profileFeed'),
    path('postMessage/', views.postMessage, name='postMessage'),
    path('profile/<int:UserId>', views.accountPage, name='accountPage'),
    path('bioUpdate/', views.bioUpdate, name='bioUpdate'),
    path('accountValidate/', views.accountValidate, name='accountValidate'),
]
