def getTask(request, search_query):
    # search_query is from the user model of the last_search value which means that the task is present in the database
    user = request.user
    latest_incomplete_task = (
        user.dailyTasks.filter(completed_at__isnull=True)
        .order_by("-created_at")
        .first()
    )
    # user has not set the last_searched  yet.
    if not search_query:
        return latest_incomplete_task

    task = user.dailyTasks.get(title=search_query)

    return task
