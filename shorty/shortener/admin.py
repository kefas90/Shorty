from django.contrib import admin
from .models import URL
# Register your models here.


class URLadmin(admin.ModelAdmin):
    fields = ("key", "url")
    list_display = ("key", "url", "created")

admin.site.register(URL)
