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
    path("videos/create/", views.createVideoListView, name="create-videos-list"),
    path(
        "videos/description/<str:pk>/",
        views.videoDescriptionView,
        name="video-description",
    ),
    path("videos/edit/<str:pk>", views.editVideoView, name="edit-video"),
    path("videos/delete/<str:pk>", views.deleteVideoView, name="delete-video"),
]
