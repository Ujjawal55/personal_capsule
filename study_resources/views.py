from django.shortcuts import render, redirect
from .forms import BookmarkForm
# Create your views here.


def resourcesListView(request):
    return render(request, "study_resources/resources_list.html")


def BookmarkView(request):
    form = BookmarkForm()

    context = {"form": form}
    return render(request, "study_resources/bookmark.html", context)
