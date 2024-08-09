from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from taskmanager.models import DailyTask
from taskmanager.forms import DailyTaskForm
# Create your views here.


def taskListView(request):
    context = {}
    return render(request, "taskmanager/tasks_list.html", context)


def dailyTaskView(request):
    user = request.user
    tasks = user.dailyTasks.all()
    context = {"tasks": tasks}
    return render(request, "taskmanager/dailytask/daily_tasks.html", context)


def createDailyTaskView(request):
    if request.method == "POST":
        form = DailyTaskForm(request.POST)
        if form.is_valid():
            daily_task = form.save(commit=False)
            daily_task.user = request.user
            daily_task.save()
            messages.success(request, "daily task have been added successfully")
            subtask_list = request.POST.getlist("subtask[]")
            for title in subtask_list:
                if title.strip():
                    daily_task.subtasks.create(daily_task=daily_task, title=title)
            return redirect("taskmanager:daily-tasks-list")
        else:
            messages.error(request, "Error in form")
    else:
        form = DailyTaskForm()
    context = {"form": form}
    return render(request, "taskmanager/dailytask/create_daily_task.html", context)


def detailDailyTaskView(request, pk):
    task = get_object_or_404(DailyTask, id=pk, user=request.user)
    context = {"task": task}
    return render(request, "taskmanager/dailytask/task_details.html", context)


def editDailyTaskView(request, pk):
    daily_task = get_object_or_404(DailyTask, id=pk, user=request.user)
    subtasks = daily_task.subtasks.all()  # type:ignore
    if request.method == "POST":
        form = DailyTaskForm(request.POST, instance=daily_task)
        if form.is_valid():
            daily_task = form.save(commit=False)
            daily_task.save()
            messages.success(request, "Changes have beens saved successfully")
            subtasksTitle = request.POST.getlist("subtask[]")

            existingSubtasks = list(daily_task.subtasks.all())

            for index, title in enumerate(subtasksTitle):
                if title.strip():
                    # if the index is less than the existing subtasks we simply update it
                    if index < len(existingSubtasks):
                        subtask = existingSubtasks[index]
                        subtask.title = title
                        subtask.save()

                    # if index is greater the existing tasks we create
                    else:
                        daily_task.subtasks.create(daily_task=daily_task, title=title)

                # if the comming subtasks list has less element than the existing one we delete the extra ones

                if len(subtasksTitle) < len(existingSubtasks):
                    for subtask in existingSubtasks[len(subtasksTitle) :]:
                        subtask.delete()

            for subtask in daily_task.subtasks.all():
                subtask.delete()
            subtask_list = request.POST.getlist("subtask[]")
            for title in subtask_list:
                if title.strip():
                    daily_task.subtasks.create(daily_task=daily_task, title=title)
            return redirect("taskmanager:details-daily-task", pk=daily_task.id)
        else:
            messages.error(request, "Error in form")

    else:
        form = DailyTaskForm(instance=daily_task)

    context = {"form": form, "subtasks": subtasks, "daily_task": daily_task}
    return render(request, "taskmanager/dailytask/edit_daily_task.html", context)


def deleteDailyTaskView(request, pk):
    task = get_object_or_404(DailyTask, id=pk, user=request.user)
    if request.method == "POST":
        task.delete()
        messages.success(request, "daily task has been deleted successfully")
        return redirect("taskmanager:daily-tasks-list")
    context = {"task": task}
    return render(request, "taskmanager/dailytask/delete_daily_task.html", context)
