from django.shortcuts import render, redirect
from .models import ResourcesList
from .forms import ResourcesListForm
# Create your views here.


def studyResourcesView(request):
    resources = ResourcesList.objects.all()
    context = {"resources": resources}
    return render(request, "study_resources/resources_list.html", context)


def createResourcesView(request):
    if request.method == "POST":
        form = ResourcesListForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("study-resources:resources-list")
    else:
        form = ResourcesListForm()
        context = {"form": form}
        return render(request, "study_resources/create_resources.html", context)
