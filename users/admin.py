from django.contrib import admin
from .models import Profile,Follow
# Register your models here.
@admin.register(Profile)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('user','bio') 
    search_fields = ('user','bio')


