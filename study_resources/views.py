from django.shortcuts import render, redirect
from .forms import BookmarkForm, VideoForm
from .models import Bookmark, Video
# Create your views here.


def resourcesListView(request):
    return render(request, "study_resources/resources_list.html")


def BookmarkView(request):
    bookmarks = Bookmark.objects.all()
    context = {"bookmarks": bookmarks}
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


def editBookmarkView(request, pk):
    bookmark = Bookmark.objects.get(id=pk)
    if request.method == "POST":
        form = BookmarkForm(request.POST, instance=bookmark)
        if form.is_valid():
            form.save()
        return redirect("study-resources:bookmarks-list")
    else:
        form = BookmarkForm(instance=bookmark)
    context = {"form": form}
    return render(request, "study_resources/bookmark/edit_bookmark.html", context)


def deleteBookmarkView(request, pk):
    bookmark = Bookmark.objects.get(id=pk)
    if request.method == "POST":
        bookmark.delete()
        return redirect("study-resources:bookmarks-list")
    else:
        form = BookmarkForm(instance=bookmark)
    context = {"form": form}
    return render(request, "study_resources/bookmark/delete_bookmark.html", context)


# started the video list views...


def videosListView(request):
    videos = Video.objects.all()
    context = {"videos": videos}
    return render(request, "study_resources/videos/videos.html", context)


def createVideoListView(request):
    if request.method == "POST":
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("study-resources:videos-list")
    else:
        form = VideoForm()
    context = {"form": form}
    return render(request, "study_resources/videos/create_video_list.html", context)
