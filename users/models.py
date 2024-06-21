from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Users(AbstractUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    profile_picture = models.ImageField(upload_to='pictures/profile_picture/', blank=True, default='default/profile_picture/user.png')
    status_message = models.TextField(blank=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f"user: {self.username}"