from django.contrib import admin
from .models import Student_user

# Register your models here.
@admin.register(Student_user)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'location']
    
