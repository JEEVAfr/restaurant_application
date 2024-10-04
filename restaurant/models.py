from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, default='Unknown Location')
    address = models.TextField()
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.IntegerField() 
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} for {self.restaurant.name}'

class Bookmark(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Use CustomUser here
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    created_at = models.DateTimeField(default=timezone.now)