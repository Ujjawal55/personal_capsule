from django.shortcuts import render

# Create your views here.


def studyResourcesView(request):
    context = {}
    return render(request, "study_resources/resources_list.html", context)
