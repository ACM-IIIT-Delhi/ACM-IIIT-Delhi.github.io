from django.contrib import admin
from . import models

admin.site.register(models.event)
admin.site.register(models.detail)
admin.site.register(models.prize)
admin.site.register(models.image)
admin.site.register(models.media)