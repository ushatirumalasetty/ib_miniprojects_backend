from django.db import models


'''
# models.py
class User(models.Model):
    name = models.CharField(max_length =100)

class Group(models.Model):
    name = models.CharField(max_length =100)
    members = models.ManyToManyField(User, through='GroupLevel')

class GroupLevel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    rank = models.IntegerField()
'''

# models.py
class Country(models.Model):
    name = models.CharField(max_length =100)
    lang = models.CharField(max_length =100)

class User(models.Model):
    name = models.CharField(max_length =100)
    lang = models.CharField(max_length =100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

class Company(models.Model):
    name = models.CharField(max_length =100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    
class Person(models.Model):
    pass

class UserLog(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    action = models.CharField(max_length =100)

