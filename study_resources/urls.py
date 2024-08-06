from django.urls import path
from study_resources import views


app_name = "study-resources"

urlpatterns = [
    path("", views.resourcesListView, name="resources-list"),
    path("bookmark/", views.BookmarkView, name="bookmarks-list"),
    path("bookmark/create/", views.createBookmarkView, name="create-bookmark"),
    path("bookmark/edit/<str:pk>", views.editBookmarkView, name="edit-bookmark"),
    path("bookmark/delete/<str:pk>", views.deleteBookmarkView, name="delete-bookmark"),
    # started the video list url
    path("videos/", views.videosListView, name="videos-list"),
]
