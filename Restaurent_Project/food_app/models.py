from django.db import models
from django.contrib.auth.models import User




class Userdeatils(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    phone=models.IntegerField(null=True)
    image=models.ImageField(upload_to='images/',null=True)



