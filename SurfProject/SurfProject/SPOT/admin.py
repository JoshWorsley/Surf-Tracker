from django.contrib import admin

# Register your models here.

from .models import Session, Surfer

admin.site.register(Session)
admin.site.register(Surfer)
