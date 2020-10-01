from django.contrib import admin
from .models import *


# Register your models here.
class DroneInline(admin.StackedInline):
    model = Drone


class DroneCategoryAdmin(admin.ModelAdmin):
    inlines = [
        DroneInline,
    ]


admin.site.register(DroneCategory, DroneCategoryAdmin,)
admin.site.register(Drone)
admin.site.register(Pilot)
admin.site.register(Competition)
