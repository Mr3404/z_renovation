from django.contrib import admin
from .models import MasterProfile


@admin.register(MasterProfile)
class MasterProfileAdmin(admin.ModelAdmin):
    list_display = ["profession", "user", "get_fullname", "get_is_staff"]

    def get_fullname(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'
    get_fullname.short_description = 'Fullname'

    def get_is_staff(self, obj):
        return obj.user.is_staff
    get_is_staff.boolean = True
    get_is_staff.short_description = "is staff"