from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=150)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    education = models.CharField(max_length=200)
    experience = models.TextField()
    skills = models.TextField()
    about = models.TextField()
    desired_position = models.CharField(max_length=150)
    github = models.URLField(blank=True)

    def __str__(self):
        return self.full_name
