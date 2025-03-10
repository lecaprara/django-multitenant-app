from django.contrib.auth.models import AbstractUser
from django.db import models
from clients.models import Client

class User(AbstractUser):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="users")

    def __str__(self):
        return self.username
