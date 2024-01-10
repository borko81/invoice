from django.contrib import admin
from . import models

admin.site.register(models.OwnerBank)
admin.site.register(models.Owner)
admin.site.register(models.Client)
admin.site.register(models.FakModels)
admin.site.register(models.FakElModels)
