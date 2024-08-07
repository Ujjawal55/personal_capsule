from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# NOTE: this method works with the vidoes and the bookmark because both have the title as search paramter
def searchQuery(request, modelClass):
    search_query = request.GET.get("search_query", "")

    if search_query == "":
        return modelClass.objects.all(), search_query

    objects = modelClass.objects.filter(title__icontains=search_query)
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
