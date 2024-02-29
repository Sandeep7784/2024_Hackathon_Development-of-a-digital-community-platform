"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from users import views as users_views
from tasks import views as task_views
from quests import views as quest_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", users_views.login, name='Login'),
    path("signup/", users_views.register, name='signup'),
    path("pending-request/" , users_views.get_pending_requests , name = 'pending-request') ,
    path("user-pending-request/" , users_views.user_pending_request , name = 'user-pending-request') ,
    path("search/" , users_views.search_query , name =  'search' ) , 
    path("request/" , users_views.send_request , name =  'request' ) ,
    path("history/", users_views.quest_history, name = 'history'),
    
]
