from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def searchQuery(request, modelname):
    search_query = request.GET.get("search_query", "")
    objects = ""
    user = request.user
    if search_query == "":
        if modelname == "video":
            return user.videos.all(), search_query
        if modelname == "bookmark":
            return user.bookmarks.all(), search_query

    if modelname == "video":
        objects = user.videos.filter(title__icontains=search_query)
        if not objects.exists():
            messages.error(request, f'No Video with title "{search_query} exist" ')
    if modelname == "bookmark":
        objects = user.bookmarks.filter(title__icontains=search_query)
        if not objects.exists():
            messages.error(request, f'No Bookmar with title "{search_query} exist" ')
    return objects, search_query


def pagination(request, object, objects_per_page):
    page_number = request.GET.get("page")
    paginator = Paginator(object, objects_per_page)

    try:
        object = paginator.page(page_number)
    except PageNotAnInteger:
        page_number = 1
        object = paginator.page(page_number)
    except EmptyPage:
        page_number = paginator.num_pages
        object = paginator.page(page_number)

    leftIndex = int(page_number) - 4

    if leftIndex <= 0:
        leftIndex = int(page_number)

    rightIndex = int(page_number) + 5

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages

    custom_range = range(leftIndex, rightIndex)

    return object, custom_range
