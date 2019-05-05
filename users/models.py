from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    # add additional fields in here
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


    def __str__(self):
        return self.email