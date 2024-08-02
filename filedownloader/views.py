from django.shortcuts import render

# Create your views here.


def fileDownload_view(request):
    return render(request, "filedownloader/index.html", {})
