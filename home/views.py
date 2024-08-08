from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from home.utils import getTask
from taskmanager.models import DailyTask
from django.utils import timezone
# NOTE: add the functionality to delete the task if all the subtask has been completed, before deleting it ask the user


def loginUser(request):
    if request.method == "POST":
        username = request.POST["username"].lower()
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home:homePage")
        else:
            print(
                "something is wrong with userid or password"
            )  # NOTE: replace with the message
    return render(request, "home/login_user.html")


def logoutUser(request):
    logout(request)
    return redirect("home:login")


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
            if is_completed:
                subtask.completed_at = timezone.now()
            else:
                subtask.completed_at = None
            subtask.save()
        return redirect("home:homePage")

    context = {"subtasks": subtasks}
    return render(request, "home/edit_subtask.html", context)
