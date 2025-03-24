"""
URL configuration for myportfolio project.

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
from django.urls import include, path
from myapp import views
from myapp.views import home, send_email, custom_404_view
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import render
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('send_email/', views.send_email, name='send_email'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'myapp.views.custom_404_view'

    