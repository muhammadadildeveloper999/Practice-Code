from django.db import models

class Message(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=200, blank=False, null=False)
    created_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.text

class message_second(models.Model):
    text = models.CharField(max_length=200, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text