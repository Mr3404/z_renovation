from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ParseError

from django.contrib.auth.models import User

from project.models import Project
from tasks.models import Task

from .serializers import TaskListSerializer, TaskDetailSerializer


class TaskListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            tasks = Task.objects.all()
            if request.user.is_staff==True:
                if request.query_params.get("status", None):
                    status = request.query_params.get("status", None)
                    tasks = tasks.filter(status=status, masters=request.user)
                    serializer = TaskListSerializer(tasks, many=True)
                    return Response(serializer.data)
                if request.query_params.get("priority", None):
                    priority = request.query_params.get("priority", None)
                    tasks = tasks.filter(priority=priority, masters=request.user)
                    serializer = TaskListSerializer(tasks, many=True)
                    return Response(serializer.data)
                tasks = tasks.filter(masters=request.user).order_by("priority", "-status")
                serializer = TaskListSerializer(tasks, many=True)
                return Response(serializer.data)
            if request.user.is_staff==False:
                tasks = tasks.filter(project__customer=request.user)
                serializer = TaskListSerializer(tasks, many=True)
                return Response(serializer.data)
            return Response({"detail":"Not Allowed"})
        except Exception as E:
            raise ParseError(E)
        

class TaskDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try:
            task = Task.objects.get(id=pk)
            if request.user.id == task.project.customer.id or task.masters.filter(id=request.user.id).exists():
                serializer = TaskDetailSerializer(task, many=False)
                return Response(serializer.data)
            return Response({"detail":"Not Allowed"})
        except Exception as E:
            raise ParseError(E)