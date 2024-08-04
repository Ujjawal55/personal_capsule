from notes.models import Notes


def searchQuery(request):
    search_query = request.GET.get("search_query", "")

    if not search_query:
        return Notes.objects.all(), search_query

    notes = Notes.objects.filter(title__icontains=search_query)

    return notes, search_query
