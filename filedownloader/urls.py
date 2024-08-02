from django.urls import path
from . import views


urlpatters = [
    path("", views.fileDownload_view, name="filedownload"),
]
