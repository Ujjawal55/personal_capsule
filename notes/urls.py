from django.urls import path
from . import views


app_name = "notes"

urlpatterns = [
    path("", views.notesListView, name="notes-list"),
    path("create/", views.createNotesView, name="create-notes"),  # type: ignore
    path("<str:pk>/", views.notesDetailView, name="notes-detail"),
    path("<str:pk>/edit", views.editNotesView, name="edit-notes"),
    path("<str:pk>/delete", views.deleteNotesView, name="delete-notes"),
    path("<str:pk>/image/", views.imageView, name="view-image"),
]
