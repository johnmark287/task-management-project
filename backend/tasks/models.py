
# tasks/models.py
from django.db import models
from django.conf import settings

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High')
    ]
    
    STATUS_CHOICES = [
        ('To Do', 'TODO'),
        ('In Progress', 'IN_PROGRESS'),
        ('Completed', 'COMPLETED')
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(
            max_length=10, 
            choices=PRIORITY_CHOICES, 
            default='MEDIUM'
        )
    status = models.CharField(
            max_length=20, 
            choices=STATUS_CHOICES, 
            default='TODO'
        )
                                         
    user = models.ForeignKey(
            settings.AUTH_USER_MODEL, 
            on_delete=models.CASCADE,
            related_name='tasks'
        )
        
    class Meta:
      ordering = ['-created_at']
    
    def __str__(self):
        return self.title