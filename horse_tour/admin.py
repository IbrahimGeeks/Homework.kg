from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Horse)
admin.site.register(models.Tourist)
admin.site.register(models.Review)
admin.site.register(models.TourCompany)
admin.site.register(models.Service)