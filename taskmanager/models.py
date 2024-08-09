from django.contrib.auth.models import User
from django.db import models
import uuid
# Create your models here.


class DailyTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dailyTasks")
    title = models.CharField(max_length=40)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return str(self.title)


class SubTask(models.Model):
    daily_task = models.ForeignKey(
        DailyTask, on_delete=models.CASCADE, related_name="subtasks"
    )
    title = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return str(self.title)
