from django.db import models

class Robot(models.Model):
    count_week = models.IntegerField(blank=False, null=False)
    model = models.CharField(max_length=2, blank=False, null=False)
    version = models.CharField(max_length=2, blank=False, null=False)
    def __str__(self):
        return self.model