from django.urls import path
from . import views


urlpatterns = [
    path("", views.fileDownload_view, name="filedownload"),
]
