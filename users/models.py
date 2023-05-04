from django.db import models
from django.contrib.auth.models import AbstractUser
from configurator.models import Modification


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11)
    image = models.ImageField(upload_to='users_image', null=True, blank=True)
    modifications = models.ManyToManyField(Modification, blank=True, related_name='modifications')
    likes = models.ManyToManyField(Modification, blank=True, related_name='liked_by')

    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users_user'