"""
URL configuration for OpenCircle project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('account/', views.account, name='account'),
    path('ui/', include('ui.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
PROJECT STRUCTURE-:
 - OpenCircle (Pre-built app 1)
    -- / [Landing page, contains signup/login form along with other introdcutory stuff]
    -- /account [Django creates account and instantly authorizes user]
    -- /ui
--The actual user interface (APP 2, under /ui)
    -- /ui/ [Contains recommended posts, notifications, friend requests etc.]
    -- /ui/post/ [When user wants to post a image or video or blog]
    -- /ui/friends/<Optional friend Name> [Shows friends list, if a specific friend is clicked then the profile of that user appears, eg /ui/friends/jared]
    -- /ui/dm/<Optional username> [Lets user see all direct messages sent to each other, by going to a specific one like /ui/dm/jared you can DM jared]

"""