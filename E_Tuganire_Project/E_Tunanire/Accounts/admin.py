from django.contrib import admin
from .models import User
# Register your models here.

# admin.site.register(User)
@admin.register(User)

class UserAdmin(admin.ModelAdmin):
    list_display=['SignUp_as','first_Name','Last_Name','Username','email','Date_of_birth','create_on','gender','genre']
    list_filter=['SignUp_as','genre']