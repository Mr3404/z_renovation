from rest_framework import serializers
from django.contrib.auth.models import User
from project.models import Project, ProjectFiles


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name", "image","start_date", "end_date"]


class ProjectFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectFiles
        fields = "__all__"


class ProjectDetailSerializer(serializers.ModelSerializer):
    files = ProjectFilesSerializer(source="projectFiles", many=True, read_only=True)
    class Meta:
        model = Project
        fields = ["id", "name", "description", "start_date", "end_date", "status", "average_price", "image", "customer", "files"]