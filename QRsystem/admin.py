from django.contrib import admin
from .models import QRcode


@admin.register(QRcode)
class QRcodeAdmin(admin.ModelAdmin):
    pass