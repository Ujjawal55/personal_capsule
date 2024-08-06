from django.urls import path
from study_resources import views


app_name = "study-resources"

urlpatterns = [
    path("", views.studyResourcesView, name="resources-list"),
    path("create/", views.createResourcesView, name="create-resources"),
]
