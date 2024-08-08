from django.urls import path
from . import views


app_name = "home"

urlpatterns = [
    path("login/", views.loginUser, name="login"),
    path("logout/", views.loginUser, name="logout"),
    path("", views.homePage, name="homePage"),
    path("edit-subtasks/<str:pk>", views.editSubtaskView, name="edit-subtasks"),
]
