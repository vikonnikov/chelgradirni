from django.contrib import admin

# Register your models here.

from core.models import Cooler

class CoolerAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name', 'performance', 'load', 'drop', 'power', 'weight', 'dimension')

admin.site.register(Cooler, CoolerAdmin)