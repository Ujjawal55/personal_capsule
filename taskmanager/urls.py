from django.urls import path
from . import views


app_name = "taskmanager"
urlpatterns = [
    path("", views.taskListView, name="tasks-list"),
]
