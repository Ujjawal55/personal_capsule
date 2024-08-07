from django.shortcuts import render

# Create your views here.


def taskListView(request):
    context = {}
    return render(request, "taskmanager/tasks_list.html", context)
