from django.shortcuts import render

# Create your views here.


def notes(request):
    context = {}
    return render(request, "notes/index.html", context)
