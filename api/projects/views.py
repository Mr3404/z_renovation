from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status
from rest_framework.exceptions import ParseError

from django.contrib.auth.models import User

from project.models import Project, ProjectFiles

from .serializers import ProjectListSerializer, ProjectDetailSerializer


class ProjectListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            projects = Project.objects.filter(customer=request.user)
            serializer = ProjectListSerializer(projects, many=True)
            return Response(serializer.data)
        except Exception as E:
            raise ParseError(E)
        

class ProjectDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try:
            project = Project.objects.get(id=pk)
            if request.user.id == project.customer.id:
                serializer = ProjectDetailSerializer(project)
                return Response(serializer.data)
            return Response({"detail":"Not allowed"}, status=403)
        except Exception as E:
            raise ParseError(E)