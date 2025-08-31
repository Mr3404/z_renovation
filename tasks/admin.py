from django.contrib import admin
from .models import Task, TaskComment, TaskFilesDone, TaskFilesToDo


class TaskFilesToDoAdmin(admin.TabularInline):
    model = TaskFilesToDo
    extra = 0


class TaskFilesDoneAdmin(admin.TabularInline):
    model = TaskFilesDone
    extra = 0


class TaskCommentAdmin(admin.TabularInline):
    model = TaskComment
    extra = 0


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = [TaskFilesToDoAdmin, TaskFilesDoneAdmin, TaskCommentAdmin]
    list_display = ["name", "start_date", "end_date", "status", "priority", "checked", "accepted"]
    list_editable = ["priority", "status", "checked", "accepted"]