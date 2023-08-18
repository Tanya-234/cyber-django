from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
            
class incidents_detail(models.Model):
    SEVERITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        )
            
    TYPE_CHOICES = (
        ('malware','malware'),
        ('phishing','phishing'),
        ('others','others'),
        )
                
    type= models.CharField(max_length=200,choices=TYPE_CHOICES)                
    description = models.TextField()
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    Report_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.type
                                    
