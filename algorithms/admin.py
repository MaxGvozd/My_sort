from django.contrib import admin
from .models import Execution


@admin.register(Execution)
class ExecutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'method', 'result')
    list_filter = ('method',)
    search_fields = ('name', 'method', 'result')
