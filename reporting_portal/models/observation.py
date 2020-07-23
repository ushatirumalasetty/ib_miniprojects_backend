from django.contrib.auth.models import AbstractUser
from django.db import models
from reporting_portal.constants.enums import *

class User (AbstractUser):
    user_name = models.CharField(max_length=50, null=False)
    user_mobile_no = models.IntegerField()
    user_profile_pic = models.URLField()
    role=models.CharField(max_length=50, choices=UserRole.get_list_of_tuples(),
                                                    default="USER")

class Category(models.Model):
    type_of_category = models.CharField(max_length=100)
    
class SubCategory(models.Model):
    sub_category = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Report(models.Model):
    title = models.TextField()
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    sub_category = models.ForeignKey(SubCategory, null=True, on_delete=models.SET_NULL)
    severity = models.CharField(max_length=50, choices=UserRole.get_list_of_tuples(),
                                                    default="USER")
