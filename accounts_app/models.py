from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    user_code=models.IntegerField()
    image=models.ImageField(upload_to='profile/image',blank=True,null=True)

    def __str__(self):
        return self.user.username






# Create your models here.

