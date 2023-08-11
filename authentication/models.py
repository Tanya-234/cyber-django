from django.db import models

from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):

    groups = models.ManyToManyField(Group, related_name='django_users')
    user_permissions = models.ManyToManyField(Permission, related_name='django_users')

    def __str__(self):
        return self.username
