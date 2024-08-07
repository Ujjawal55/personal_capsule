from taskmanager.models import DailyTask


def getTask(search_query):
    if not search_query:
        latest_incomplete_task = (
            DailyTask.objects.filter(completed_at__isnull=True)
            .order_by("-created_at")
            .first()
        )

        return latest_incomplete_task
    task = (
        DailyTask.objects.filter(title__icontains=search_query)
        .order_by("-created_at")
        .first()
    )
    return task
