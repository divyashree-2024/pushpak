from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    college = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)


class UserAddress(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    address_name = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    address_city = models.CharField(max_length=100)
    address_state = models.CharField(max_length=100)
    address_country = models.CharField(max_length=100)
    address_pincode = models.CharField(max_length=6)

