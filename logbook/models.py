from django.conf import settings
from django.db import models
from django.utils import timezone

class Diver(models.Model):
    account = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    certification_org = models.CharField(max_length=100)
    certification_level = models.CharField(max_length=100)
    certification_date = models.DateField()

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_date_of_last_dive(self):
        return self.dives.latest('date').date

class Dive(models.Model):
    diver = models.ForeignKey(Diver, on_delete=models.CASCADE, related_name='dives')
    location = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    duration = models.DurationField()
    max_depth = models.IntegerField()
    buddy_name = models.CharField(max_length=100)
    log_text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s %s' % (self.date, self.location)
