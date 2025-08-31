from django.db import models
from django.contrib.auth.models import User



class Project(models.Model):
    STATUS_CHOICES = [
        ('ready_to_start','Ready to start'),
        ('active', 'Active'),
        ('on_hold', 'On Hold'),
        ('completed', 'Completed'),
    ]
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="project", verbose_name="Customer",limit_choices_to={'is_staff': False})
    name = models.CharField(max_length=255, verbose_name="Project Name")
    description = models.TextField(verbose_name="Description")
    start_date = models.DateField(auto_now_add=False)
    end_date = models.DateField(auto_now_add=False, blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, default="ready to start")
    average_price = models.DecimalField(max_digits=15, decimal_places=2)
    image = models.ImageField(upload_to="project_image/", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name
    

class ProjectFiles(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="projectFiles")
    file = models.FileField(upload_to="projectFiles/", blank=True, null=True)