from django.shortcuts import redirect, render

from taskmanager.models import DailyTask
from taskmanager.forms import DailyTaskForm
# Create your views here.


def taskListView(request):
    context = {}
    return render(request, "taskmanager/tasks_list.html", context)


def dailyTaskView(request):
    tasks = DailyTask.objects.all()
    context = {"tasks": tasks}
    return render(request, "taskmanager/dailytask/daily_tasks.html", context)


def createDailyTaskView(request):
    if request.method == "POST":
        form = DailyTaskForm(request.POST)
        if form.is_valid():
            daily_task = form.save()
            subtask_list = request.POST.getlist("subtask[]")
            for title in subtask_list:
                if title.strip():
                    daily_task.subtasks.create(daily_task=daily_task, title=title)
            return redirect("taskmanager:daily-tasks-list")
    else:
        form = DailyTaskForm()
    context = {"form": form}
    return render(request, "taskmanager/dailytask/create_daily_task.html", context)


def detailDailyTaskView(request, pk):
    task = DailyTask.objects.get(id=pk)
    context = {"task": task}
    return render(request, "taskmanager/dailytask/task_details.html", context)


def editDailyTaskView(request, pk):
    daily_task = DailyTask.objects.get(id=pk)
    subtasks = daily_task.subtasks.all()  # type:ignore
    if request.method == "POST":
        form = DailyTaskForm(request.POST, instance=daily_task)
        if form.is_valid():
            daily_task = form.save()
            subtask_list = request.POST.getlist("subtask[]")
            for title in subtask_list:
                if title.strip():
                    daily_task.subtasks.create(daily_task=daily_task, title=title)
            return redirect("taskmanager:details-daily-task", pk=daily_task.id)

    else:
        form = DailyTaskForm(instance=daily_task)

    context = {"form": form, "subtasks": subtasks, "daily_task": daily_task}

    return render(request, "taskmanager/dailytask/edit_daily_task.html", context)


def deleteDailyTaskView(request, pk):
    task = DailyTask.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect("taskmanager:daily-tasks-list")
    context = {"task": task}
    return render(request, "taskmanager/dailytask/delete_daily_task.html", context)
