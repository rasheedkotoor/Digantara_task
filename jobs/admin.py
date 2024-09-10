from django.contrib import admin
from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'interval', 'last_run', 'next_run', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('interval',)
