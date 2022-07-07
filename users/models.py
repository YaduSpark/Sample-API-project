from django.db import models
from django.contrib.auth.models import User


class newUser(User):
    pass


class Profile(models.Model):
    user = models.OneToOneField(newUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    joinedDate = models.DateTimeField(auto_now_add=True)
