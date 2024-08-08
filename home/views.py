from django.shortcuts import render, redirect
from home.utils import getTask
from taskmanager.models import DailyTask


def homePage(request):
    task = getTask("")
    context = {"task": task}
    return render(request, "home/index.html", context)


def editSubtaskView(request, pk):
    task = DailyTask.objects.get(id=pk)
    subtasks = task.subtasks.all()  # type: ignore
    if request.method == "POST":
        for subtask in subtasks:
            is_completed = (
                request.POST.get(f"subtask_completed_{subtask.id}")
            ) == "true"
            subtask.is_completed = is_completed
            subtask.save()
        return redirect("home:homePage")

    context = {"subtasks": subtasks}
    return render(request, "home/edit_subtask.html", context)
