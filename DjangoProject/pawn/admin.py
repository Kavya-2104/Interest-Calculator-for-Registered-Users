from django.contrib import admin

# Register your models here.
from . import models
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name',)

admin.site.register(models.Profile,ProfileAdmin)