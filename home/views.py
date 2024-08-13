from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from home.forms import CustomUserCreationForm, ProfileForm
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
            messages.success(request, "you have been successfully logged in")
            return redirect("home:homePage")
        else:
            messages.error(request, "Username or password is wrong")
    return render(request, "home/login_user.html")


def logoutUser(request):
    logout(request)
    messages.success(request, "you have been logout")
    return redirect("home:login")


def registerUserView(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            message = f"hello {user.username}, you have been successfully registered"
            messages.success(request, message)
            return redirect("home:login")
        else:
            messages.error(request, "some error has been occured in registration")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "home/user_registration.html", context)


def homePage(request):
    profile = request.user.profile
    task = getTask(request, profile.last_search)
    context = {"task": task, "profile": profile}
    return render(request, "home/index.html", context)


def editSubtaskView(request, pk):
    task = DailyTask.objects.get(id=pk)
    subtasks = task.subtasks.all()  # type: ignore
    count = 0
    if request.method == "POST":
        for subtask in subtasks:
            is_completed = (
                request.POST.get(f"subtask_completed_{subtask.id}")
            ) == "true"
            subtask.is_completed = is_completed
            if is_completed:
                subtask.completed_at = timezone.now()
                count = count + 1
            else:
                subtask.completed_at = None
            if count == 1:
                messages.success(
                    request,
                    f'congratulation, you have successfully completed "{subtask.title}" task',
                )
            if count not in [0, 1]:
                messages.success(
                    request,
                    f"congratulation, you have successfully completed {count} tasks",
                )
            subtask.save()
        messages.success(request, "changes have been saved successfully")
        return redirect("home:homePage")
    context = {"subtasks": subtasks}
    return render(request, "home/edit_subtask.html", context)


def searchTaskView(request):
    user = request.user
    if request.method == "POST":
        search_query = request.POST.get("title", "").strip()
        # first check if the exact match is found or not
        try:
            dailyTask = user.dailyTasks.get(title=search_query)
        except DailyTask.DoesNotExist:  # type: ignore
            # check if the task have the matching pattern
            dailyTasks = user.dailyTasks.filter(title__icontains=search_query)
            if dailyTasks.exists():
                dailyTask = dailyTasks.order_by("-created_at").first()
            else:
                dailyTask = None

        if dailyTask is None:
            messages.error(request, "title does not exist")
            return redirect("home:search-task")

        user.profile.last_search = dailyTask.title
        user.profile.save()
        return redirect("home:homePage")

    return render(request, "home/search_task.html")


def editProfileView(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been edited successfully")
            return redirect("home:homePage")
        else:
            messages.error(request, "Some error in form")
            return redirect("home:edit-profile")
    context = {"form": form}
    return render(request, "home/edit_profile.html", context)
