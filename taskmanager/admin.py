from django.contrib import admin

from taskmanager.models import DailyTask, SubTask

# Register your models here.

admin.site.register(DailyTask)
admin.site.register(SubTask)
