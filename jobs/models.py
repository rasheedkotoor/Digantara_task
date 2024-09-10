from django.db import models
from datetime import timedelta


class Job(models.Model):
    INTERVAL_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('custom', 'Custom Interval')
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    last_run = models.DateTimeField(null=True, blank=True)
    next_run = models.DateTimeField(null=True, blank=True)
    interval = models.CharField(max_length=50, choices=INTERVAL_CHOICES)
    custom_interval_days = models.PositiveIntegerField(null=True, blank=True, help_text="For custom interval (in days)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def update_next_run(self):
        """Update the next_run time based on the interval."""
        if self.interval == 'daily':
            self.next_run = self.last_run + timedelta(days=1)
        elif self.interval == 'weekly':
            self.next_run = self.last_run + timedelta(weeks=1)
        elif self.interval == 'monthly':
            # Assuming 30 days for a month, you can adjust this if needed
            self.next_run = self.last_run + timedelta(days=30)
        elif self.interval == 'custom' and self.custom_interval_days:
            self.next_run = self.last_run + timedelta(days=self.custom_interval_days)
        else:
            self.next_run = None

    def __str__(self):
        return self.name
