from django.contrib import admin
from .models import Www


@admin.register(Www)
class wwwAdmin(admin.ModelAdmin):
    pass
