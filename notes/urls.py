from django.urls import path
from . import views


urlpatterns = [
    path("", views.notesListView, name="notes-list"),
    path("create/", views.createNotesView, name="create-notes"),  # type: ignore
    path("edit/<str:pk>", views.editNotesView, name="edit-notes"),
    path("<str:pk>/", views.notesDetailView, name="notes-detail"),
]
