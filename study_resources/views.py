from django.shortcuts import render, redirect
from .forms import BookmarkForm
# Create your views here.


def resourcesListView(request):
    return render(request, "study_resources/resources_list.html")


def BookmarkView(request):
    context = {}
    return render(request, "study_resources/bookmark/bookmark.html", context)


def createBookmarkView(request):
    if request.method == "POST":
        form = BookmarkForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(
            "study-resources:bookmarks-list"
        )  # TODO: redirect the user to the bookmark not to the list
    else:
        form = BookmarkForm()
        context = {"form": form}

        return render(request, "study_resources/bookmark/create_bookmark.html", context)
