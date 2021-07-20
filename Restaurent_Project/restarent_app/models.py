from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class RestaurentModel(models.Model):
    rest_id=models.IntegerField(null=True)
    rest_username=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    rest_name=models.CharField(max_length=30,null=True)
    rest_image=models.FileField(null=True)
    rest_type=models.CharField(max_length=36,null=True)
    rest_status=models.CharField(max_length=10,null=True)
    rest_city=models.CharField(max_length=20,null=True)
    rest_state=models.CharField(max_length=20,null=True)
    rest_ratings=models.CharField(max_length=3,null=True,default=2.5)
    rest_pincode=models.IntegerField(null=False,default=False)
    rest_address=models.CharField(max_length=50,null=False,default=False)

    def __int__(self):
        return self.rest_name

class AddFoodModel(models.Model):
    fid=models.IntegerField(null=False,default=False)
    rname=models.CharField(max_length=30,null=False)
    dname=models.CharField(max_length=40,null=False)
    dtype=models.CharField(max_length=19,null=False)
    dcat=models.CharField(max_length=20,null=True)
    dprice=models.IntegerField(null=False)
    image1=models.FileField (null=False)
    image2=models.FileField (null=False)
    image3=models.FileField (null=True)


    def __int__(self):
        return self.rname

class AddtocartModel(models.Model):
    usr=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    pro=models.ForeignKey(AddFoodModel,on_delete=models.CASCADE,null=True)
    created_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.pro.dname


class OredrModel(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    oid= models.CharField(max_length=50, null=False,default=True)
    rname= models.CharField(max_length=50, null=False,default=True)
    dname= models.CharField(max_length=50, null=False,default=True)
    dcat= models.CharField(max_length=50, null=False,default=True)
    dtype= models.CharField(max_length=50, null=False,default=True)
    dprice= models.CharField(max_length=50, null=False,default=True)
    quantity = models.IntegerField(null=True, default=1)
    mobile = models.IntegerField(null=True, )
    fullname = models.CharField(max_length=50, null=False)
    address1 = models.CharField(max_length=50, null=False)
    payment_status = models.CharField(max_length=500, default='Not Done')
    amount = models.FloatField(null=True)
    order_status = models.CharField(max_length=50, null=True, )
    created_at=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.dname


class PromosModel(models.Model):
    promo_id=models.CharField(max_length=10,null=False)
    promo_code=models.CharField(max_length=20,null=False)
    prome_name=models.CharField(max_length=20,null=True)
    promo_discription=models.CharField(max_length=100,null=True)
    is_active=models.BooleanField(null=True)
    valid_upto=models.DateTimeField(null=True)

    def __str__(self):
        return self.prome_name
