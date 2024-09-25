"""
URL configuration for WingCol project.

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
from .views import *
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', get_all_users),
    path('users/<int:id>', get_user),
    path('users/client/<int:id>', get_client), 
    path('users/client/create/', create_client),
    path('users/client/update/', update_client),
    path('users/client/delete/<int:id>', delete_client),
    path('users/admin/create/', create_admin),
    path('users/admin/update/', update_admin),
    path('users/admin/delete/<int:id>', delete_admin),
    path('users/login/', login),
]
