from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=CASCADE)
    photo=models.ImageField(upload_to='users', blank=True, null=True)
    date_of_birth=models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} profili'
