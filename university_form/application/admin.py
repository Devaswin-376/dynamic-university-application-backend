from django.contrib import admin
from .models import University, ApplicationField

class ApplicationFieldInline(admin.TabularInline):
    model = ApplicationField
    extra = 1

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location','description')
    inlines = [ApplicationFieldInline]

@admin.register(ApplicationField)
class ApplicationFieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'university', 'field_type', 'is_required')
    list_filter = ('university', 'field_type')
