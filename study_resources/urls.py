from django.urls import path
from study_resources import views


app_name = "study-resources"

urlpatterns = [
    path("", views.resourcesListView, name="resources-list"),
    path("bookmark/", views.BookmarkView, name="bookmark"),
]
