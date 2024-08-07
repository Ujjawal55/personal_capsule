from django.urls import path
from . import views


app_name = "taskmanager"
urlpatterns = [
    path("", views.taskListView, name="tasks-list"),
    path("daily-task/", views.dailyTaskView, name="daily-tasks-list"),
    path("daily-task/create/", views.createDailyTaskView, name="create-daily-task"),
    path(
        "daily-task/details/<str:pk>",
        views.detailDailyTaskView,
        name="details-daily-task",
    ),
    path(
        "daily-task/edit/<str:pk>",
        views.editDailyTaskView,
        name="edit-daily-task",
    ),
    path(
        "daily-task/delete/<str:pk>",
        views.deleteDailyTaskView,
        name="delete-daily-task",
    ),
]
