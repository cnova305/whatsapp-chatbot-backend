from email import message
from django.db import models

# Create your models here.

class WhatsAppMessage(models.Model):
    messageSender = models.CharField(max_length=200)
    messageBody = models.CharField(max_length=5000)

    def ___str___(self):
        return self.messageSender, self.messageBody