from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from api.auth.views import UserRegisterWithTokenView, UserDetailView
from api.projects.views import ProjectListView, ProjectDetailView
from api.tasks.views import TaskListView, TaskDetailView


urlpatterns = [
    path("register/", UserRegisterWithTokenView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    
    path("projects/", ProjectListView.as_view(), name="projects"),
    path("project/<int:pk>/", ProjectDetailView.as_view(), name="project"),

    path("tasks/", TaskListView.as_view(), name="tasks"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task"),
]