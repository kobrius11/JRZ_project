from django.contrib import admin
from . import models


admin.site.register(models.Manager)
admin.site.register(models.Employee)
admin.site.register(models.Application)
admin.site.register(models.ApplicationInstance)
admin.site.register(models.Department)

admin.site.register(models.Vacation)
admin.site.register(models.ParentDayOff)
admin.site.register(models.Taxes)
admin.site.register(models.Termination)