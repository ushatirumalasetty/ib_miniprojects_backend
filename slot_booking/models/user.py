from django.contrib.auth.models import AbstractUser
from django.db import models
from slot_booking.constants.enums import *

class User (AbstractUser):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    user_name = models.CharField(max_length=50, null=False)
    role=models.CharField(max_length=50, choices=UserRole.get_list_of_tuples(),
                         default="USER")

class WashingMachine(models.Model):
    washing_machine_id = models.CharField(max_length=50, null=False)
    status= models.CharField(
      max_length=10,
      choices=[(washing_machine_status.name,washing_machine_status.value)
               for washing_machine_status in WashingMachineStatus],
               default = "ACTIVE"
    )

class WashingMachineSlot(models.Model):
    washing_machine = models.ForeignKey(WashingMachine,
                             on_delete=models.CASCADE,
                             related_name='washing_machine_bookings')
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=False)
    day= models.CharField(
      max_length=10,
      choices=[(day.name,day.value) for day in Days]
    )


class UserSlot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=False)
    washing_machine_slot= models.ForeignKey(WashingMachineSlot, on_delete=models.CASCADE,
                             null=False)
    date = models.DateField(null=False)
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=False)

class DaysRange(models.Model):
    days_range = models.IntegerField(null=False)


class Request(models.Model):
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    date = models.DateField(null=False)
    requested_user_slot = models.ForeignKey(UserSlot, on_delete=models.CASCADE,
                                 null=False)
    request_status= models.CharField(
      max_length=10,
      choices=[(request_status.name,request_status.value)
               for request_status in RequestStatus],
               default = "PENDING"
    )
