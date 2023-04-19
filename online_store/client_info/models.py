from django.db import models


# Create your models here.
#User profile to which the user must login
class Userprofile(models.Model):
    owner = models.OneToOneField('auth.User', related_name='UserProfile', on_delete=models.CASCADE)