from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from .forms import BookmarkForm, VideoForm
from .models import Bookmark, Video
from .utils import searchQuery, pagination
# Create your views here.


def resourcesListView(request):
    return render(request, "study_resources/resources_list.html")


def BookmarkView(request):
    bookmarks, search_query = searchQuery(request, "bookmark")
    bookmarks, custom_range = pagination(request, bookmarks, 3)

    context = {
        "bookmarks": bookmarks,
        "search_query": search_query,
        "custom_range": custom_range,
    }
    return render(request, "study_resources/bookmark/bookmark.html", context)


def createBookmarkView(request):
    if request.method == "POST":
        form = BookmarkForm(request.POST)
        if form.is_valid():
            bookmark = form.save(commit=False)
            bookmark.user = request.user
            bookmark.save()
            messages.success(request, "bookmark has been added successfully")
            return redirect("study-resources:bookmarks-list")
        else:
            messages.error(request, "Error in the form")
    else:
        form = BookmarkForm()
    context = {"form": form}

    return render(request, "study_resources/bookmark/create_bookmark.html", context)


def editBookmarkView(request, pk):
    bookmark = get_object_or_404(Bookmark, id=pk, user=request.user)
    if request.method == "POST":
        form = BookmarkForm(request.POST, instance=bookmark)
        if form.is_valid():
            updated_bookmark = form.save(commit=False)
            updated_bookmark.save()
            messages.success(request, "changes have been saved successfully")
            return redirect("study-resources:bookmarks-list")
        else:
            messages.error(request, "Error in the form")
    else:
        form = BookmarkForm(instance=bookmark)
    context = {"form": form}
    return render(request, "study_resources/bookmark/edit_bookmark.html", context)


def deleteBookmarkView(request, pk):
    bookmark = get_object_or_404(Bookmark, id=pk, user=request.user)
    if request.method == "POST":
        bookmark.delete()
        messages.success(request, "Bookmark have been deleted successfully")
        return redirect("study-resources:bookmarks-list")
    else:
        form = BookmarkForm(instance=bookmark)
    context = {"form": form}
    return render(request, "study_resources/bookmark/delete_bookmark.html", context)


# started the video list views...


def videosListView(request):
    videos, search_query = searchQuery(request, "video")
    videos, custom_range = pagination(request, videos, 3)
    context = {
        "videos": videos,
        "search_query": search_query,
        "custom_range": custom_range,
    }
    return render(request, "study_resources/videos/videos.html", context)


def createVideoListView(request):
    if request.method == "POST":
        form = VideoForm(request.POST)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            messages.success(request, "Video has been added successfully")
            return redirect("study-resources:videos-list")
        else:
            messages.error(request, "Error in the form")
    else:
        form = VideoForm()
    context = {"form": form}
    return render(request, "study_resources/videos/create_video_list.html", context)


def videoDescriptionView(request, pk):
    video = get_object_or_404(Video, id=pk, user=request.user)
    context = {"video": video}
    return render(
        request, "study_resources/videos/view_video_description.html", context
    )


def editVideoView(request, pk):
    video = get_object_or_404(Video, id=pk, user=request.user)
    if request.method == "POST":
        form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            video = form.save(commit=False)
            video.save()
            messages.success(request, "changes have been saved successfully")
            return redirect("study-resources:video-description", pk=video.id)
        else:
            messages.error(request, "Error in the form")
    else:
        form = VideoForm(instance=video)
    context = {"form": form}
    return render(request, "study_resources/videos/video_edit.html", context)


def deleteVideoView(request, pk):
    video = get_object_or_404(Video, id=pk, user=request.user)
    if request.method == "POST":
        video.delete()
        messages.success(request, "Video has been deleted successfully")
        return redirect("study-resources:videos-list")
    else:
        form = VideoForm(instance=video)
    context = {"form": form}
    return render(request, "study_resources/videos/delete_video.html", context)
