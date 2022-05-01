from django.contrib import admin
from .models import WhatsAppMessage

# Register your models here.

class WhatsAppMessageAdmin(admin.ModelAdmin):
    list = ( 'messageSender', 'messageBody')

    admin.site.register(WhatsAppMessage)
