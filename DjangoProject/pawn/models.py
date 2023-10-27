from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    profile_id = models.AutoField
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    amount = models.FloatField()
    interest = models.FloatField()
    month = models.IntegerField()
    phnno = models.IntegerField()
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    collateral = models.CharField(max_length=300)
    address = models.CharField(max_length=400)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="pawn")



