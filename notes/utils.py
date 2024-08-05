from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from notes.models import Notes


def searchQuery(request):
    search_query = request.GET.get("search_query", "")

    if not search_query:
        return Notes.objects.all(), search_query

    notes = Notes.objects.filter(title__icontains=search_query)

    return notes, search_query


def pagination(request, projects, objects_per_page):
    page_number = request.GET.get("page")

    paginator = Paginator(projects, objects_per_page)

    try:
        projects = paginator.page(page_number)
    except PageNotAnInteger:
        page_number = 1
        projects = paginator.page(page_number)
    except EmptyPage:
        page_number = paginator.num_pages
        projects = paginator.page(page_number)

    leftIndex = int(page_number) - 4

    if leftIndex <= 0:
        leftIndex = 1

    rightIndex = int(page_number) + 3

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages

    custom_range = range(leftIndex, rightIndex)

    return projects, custom_range
