from django.db import models

class Wine(models.Model):
    name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    region = models.CharField(max_length=100, blank=True)
    grape = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.year})"
