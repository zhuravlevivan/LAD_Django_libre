"""
URL configuration for libre project.

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
from django.urls import path, include
from libre_authors.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('libre_authors.urls')),
    path('users/', include('users.urls', namespace='users')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

]

handler404 = page_not_found
admin.site.site_header = 'ADMIN PANEL'
admin.site.index_title = 'LIBRARY'
