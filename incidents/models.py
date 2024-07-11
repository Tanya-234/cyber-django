from django.db import models
from django.utils import timezone
from authentication.models import User
            
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
    
    STATUS_CHOICES = (
        ('In progress','In progress'),
        ('Resolved','Resolved'),
        ('Closed','Closed')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)           
    type= models.CharField(max_length=200,choices=TYPE_CHOICES)                
    description = models.TextField()
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    Report_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=200,choices=STATUS_CHOICES)
    evidence = models.FileField(upload_to='evidence/', blank=True, null=True)
    def __str__(self):
        return self.type

    

                                    
