from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def searchQuery(request):
    user = request.user
    search_query = request.GET.get("search_query", "")

    if not search_query:
        return user.notes.all(), search_query

    notes = user.notes.filter(title__icontains=search_query)

    if not notes.exists():
        messages.error(request, f'No notes with title "{search_query}" exist')

    return notes, search_query


def pagination(request, notes, objects_per_page):
    page_number = request.GET.get("page")

    paginator = Paginator(notes, objects_per_page)

    try:
        notes = paginator.page(page_number)
    except PageNotAnInteger:
        page_number = 1
        notes = paginator.page(page_number)
    except EmptyPage:
        page_number = paginator.num_pages
        notes = paginator.page(page_number)

    leftIndex = int(page_number) - 2

    if leftIndex <= 0:
        leftIndex = 1

    rightIndex = int(page_number) + 2

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages

    custom_range = range(leftIndex, rightIndex)

    return notes, custom_range
