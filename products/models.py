from django.db import models
from django.conf import settings
from django.utils import timezone

class Tour(models.Model):
    title = models.CharField(max_length=255, default="no title")
    description = models.TextField(default="no description")
    duration = models.PositiveIntegerField(default=2)
    price = models.FloatField(default=1.0, null=False)
    location = models.CharField(max_length=255, default="no location", null=False)
    created_at = models.DateTimeField(default=timezone.now)

class Request(models.Model):
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('confirmed', 'Confirmed'),
        ('complete', 'Complete'),
        ('refused', 'Refused'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='requests')
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='requests')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ongoing')
    scheduled_date = models.DateField()
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)