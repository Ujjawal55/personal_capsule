from django.contrib import messages
from django.shortcuts import redirect
from taskmanager.models import DailyTask
# NOTE: case handle here


def getTask(request, search_query):
    user = request.user
    latest_incomplete_task = ""
    if not search_query:
        latest_incomplete_task = (
            user.dailyTasks.filter(completed_at__isnull=True)
            .order_by("-created_at")
            .first()
        )

        return latest_incomplete_task
    task = (
        user.dailyTasks.filter(title__icontains=search_query)
        .order_by("-created_at")
        .first()
    )

    if task is None:
        messages.error(request, "search task does not exist")
        return redirect("home:homePage")
    return task
