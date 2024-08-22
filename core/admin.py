from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User

@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'phone_number', 'date_of_birth')
    search_fields = ('email', 'full_name')
    fields = ('email', 'full_name', 'phone_number', 'date_of_birth')