from django.db import models
from django.contrib.auth.models import User
from project.models import Project


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ]
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]
    name = models.CharField(max_length=255, verbose_name="Task name")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="task", verbose_name="project")
    description = models.TextField(verbose_name="Description")
    masters = models.ManyToManyField(User, limit_choices_to={"is_staff":True}, verbose_name="Master")
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=10, verbose_name="Priority", default="medium")
    status = models.CharField(choices=STATUS_CHOICES, max_length=15, verbose_name="Status", default="todo")
    checked = models.BooleanField(default=False, verbose_name="Checked By Manager")
    accepted = models.BooleanField(default=False, verbose_name="Accepted by Customer")
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date")


    class Meta:
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.name


class TaskFilesToDo(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="taskFilesToDo", verbose_name="task")
    files = models.FileField(upload_to="taskFilesToDo/", blank=True, null=True)

    class Meta:
        verbose_name_plural = "To Do Files"


class TaskFilesDone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="taskFilesDoneUser", verbose_name="user", limit_choices_to={"is_staff":True})
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="taskFilesDone", verbose_name="task")
    files = models.FileField(upload_to="taskFilesDone/", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Done Files"


class TaskComment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="taskComment", verbose_name="task")
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="taskCommentUser", verbose_name="user")
    text = models.TextField(verbose_name="Text", blank=True, null=True)
    file = models.FileField(upload_to="TaskCommentFiles/", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Comments"