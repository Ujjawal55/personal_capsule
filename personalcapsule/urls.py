"""
URL configuration for personalcapsule project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from home import urls as home_urls
from filedownloader import urls as filedownloader_urls
from notes import urls as notes_urls
from study_resources import urls as study_resources_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(home_urls, namespace="home")),
    path("filedownloader/", include(filedownloader_urls)),
    path("notes/", include(notes_urls, namespace="notes")),
    path(
        "study-resources/", include(study_resources_urls, namespace="study-resources")
    ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
