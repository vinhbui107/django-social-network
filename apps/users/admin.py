from django.contrib import admin
from .models import CustomUser, Follow


admin.site.register(CustomUser)
admin.site.register(Follow)
