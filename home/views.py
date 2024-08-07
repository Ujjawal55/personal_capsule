from django.shortcuts import render
from home.utils import getTask


def homePage(request):
    task = getTask("")
    context = {"task": task}
    return render(request, "home/index.html", context)
