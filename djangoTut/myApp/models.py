from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Keep ONLY this single version of FirstModel
class FirstModel(models.Model):
    TECH_STACK_CHOICE=[
        ('PY', 'PYTHON'),
        ('JS', 'JAVASCRIPT'),
        ('RD', 'REDIS')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='test/')
    date_added = models.DateTimeField(default=timezone.now)
    tech = models.CharField(max_length=2, choices=TECH_STACK_CHOICE)

    def __str__(self):
        return self.name


# One to Many Relationship Implementation
class EngineerReview(models.Model):
    RATING_CHOICES = [
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    ]
    
    first_model = models.ForeignKey(
        FirstModel, 
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE) # The new non-nullable field
    review_text = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    date_reviewed = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Review by {self.user} on {self.first_model.name}"


# Many to Many
class Store(models.Model):
    first_models = models.ManyToManyField(
        FirstModel,
        related_name='stores'
    )
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} ({self.location})"
    

# One to One
class ProfileExpansion(models.Model):
    first_model = models.OneToOneField(
        FirstModel,
        on_delete=models.CASCADE,
        related_name='expansion'
    )
    website_url = models.URLField(blank=True, null=True)
    internal_notes = models.TextField(blank=True)

    def __str__(self):
        return f"Expansion Details for {self.first_model.name}"
