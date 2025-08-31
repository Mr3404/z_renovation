from django.contrib import admin
from .models import Project, ProjectFiles


class ProjectFilesAdminInline(admin.TabularInline):
    model = ProjectFiles
    extra = 0


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "get_customer", "average_price", "start_date", "end_date"]
    inlines = [ProjectFilesAdminInline]

    def get_customer(self, obj):
        return f"{obj.customer.first_name} {obj.customer.last_name}"
    get_customer.short_description = "Customer"