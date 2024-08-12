from django.urls import path
from . import views


app_name = "home"

urlpatterns = [
    path("login/", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register-user/", views.registerUserView, name="register"),
    path("create-profile/", views.createProfileView, name="create-profile"),
    path("", views.homePage, name="homePage"),
    path("edit-subtasks/<str:pk>", views.editSubtaskView, name="edit-subtasks"),
    path("search-task/", views.searchTaskView, name="search-task"),
]
