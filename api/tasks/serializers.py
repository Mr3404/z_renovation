from rest_framework import serializers
from django.contrib.auth.models import User

from tasks.models import Task, TaskComment, TaskFilesToDo, TaskFilesDone


class TaskCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskComment
        fields = "__all__"


class TaskFilesToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskFilesToDo
        fields = "__all__"


class TaskFilesDoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskFilesDone
        fields = "__all__"


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "name", "project", "start_date", "end_date", "priority", "status", "checked", "accepted"]


class TaskDetailSerializer(serializers.ModelSerializer):
    comments = TaskCommentSerializer(source="taskComment", many=True, read_only=True)
    class Meta:
        model = Task
        fields = ["id", "name", "description", "project", "masters", "priority", "status", "start_date", "end_date", "checked", "accepted", "comments"]