from django.contrib import admin
from .models import Response

# Register your models here.


class ResponseAdmin(admin.ModelAdmin):
    model = Response


admin.site.register(Response, ResponseAdmin)