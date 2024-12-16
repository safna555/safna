"""
URL configuration for demo2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from myuser import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home2/', views.home),
    path('content/', views.add_book),
    path('delete/<int:id>', views.delete),
    path('update/<int:id>', views.update),
    path('viewmore/<int:id>', views.viewmore),
    path('',views.login),
    path('register/',views.register),
    path('login/',views.logout),
] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
