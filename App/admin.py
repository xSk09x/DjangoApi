from django.contrib import admin
from django.contrib.admin import ModelAdmin
from App.models import Plant


# Register your models here.
@admin.register(Plant)
class PlantAdmin(ModelAdmin):
    pass