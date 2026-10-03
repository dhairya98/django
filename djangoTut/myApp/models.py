from django.db import models
from django.utils import timezone

# Create your models here.
class FirstModel(models.Model):
    TECH_STACK_CHOICE=[
        ('PY', 'PYTHON'),
        ('JS', 'JAVASCRIPT'),
        ('RD', 'REDIS')
    ]
    name= models.CharField(max_length=100)
    image= models.ImageField(upload_to='test/')
    date_added=models.DateTimeField(default=timezone.now)
    tech=models.CharField(max_length=2, choices=TECH_STACK_CHOICE)