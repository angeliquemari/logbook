from django.conf import settings
from django.db import models
from django.utils import timezone

class Diver(models.Model):
    account = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    certification_org = models.CharField(max_length=100)
    certification_level = models.CharField(max_length=100)
    certification_date = models.DateField()

class Dive(models.Model):
    diver = models.ForeignKey(Diver, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    duration = models.DurationField()
    max_depth = models.IntegerField()
    buddy_name = models.CharField(max_length=100)
    log_text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
