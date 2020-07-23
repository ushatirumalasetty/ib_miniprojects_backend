import pytest
from slot_booking.models.user import *
from datetime import time,date

@pytest.fixture()
def create_users():
    users = [
        {
            'username': 'user1',
            "first_name": "John",
            "last_name":"abhi"
        },
        {
            'username': 'user2',
            "first_name": "Johny",
            "last_name":"abhiram"     
        }
    ]

    for user in users:
        User.objects.create(
            username=user['username'],
            first_name=user['first_name'],
            last_name=user['last_name'])

@pytest.fixture()
def create_washing_machines():
    washing_machines = [
        {
            "washing_machine_id" : 'wm1',
            "status" : "ACTIVE"
        },
        {
            "washing_machine_id" : 'wm2',
            "status" : "INACTIVE"
        }
    ]
    for washing_machine in washing_machines:
        WashingMachine.objects.create(
            washing_machine_id=washing_machine['washing_machine_id'],
            status=washing_machine['status'])


@pytest.fixture()
def create_washing_machine_slots():
    washing_machine_slots = [
        {
            "washing_machine_id" : 1,
            "day":"SUNDAY",
            "start_time": time(5),
            "end_time": time(6)
        },
        {
            "washing_machine_id" : 1,
            "day":"MONDAY",
            "start_time": time(7),
            "end_time": time(8)
        }
    ]
    for washing_machine_slot in washing_machine_slots:
        WashingMachineSlot.objects.create(
            washing_machine_id=washing_machine_slot['washing_machine_id'],
            day=washing_machine_slot['day'],
            start_time=washing_machine_slot['start_time'],
            end_time=washing_machine_slot['end_time'])

@pytest.fixture()
def create_user_slots():
    user_slots = [
        {
            "user_id":1,
            "washing_machine_id" : 1,
            "date":date(2020,1,1),
            "start_time": time(5),
            "end_time": time(6)
        },
        {
            "user_id":1,
            "washing_machine_id" : 1,
            "date":date(2020,11,11),
            "start_time": time(7),
            "end_time": time(8)
        },
    ]
    for user_slot in user_slots:
        UserSlot.objects.create(
            user_id=user_slot["user_id"],
            washing_machine_id=user_slot['washing_machine_id'],
            date=user_slot['date'],
            start_time=user_slot['start_time'],
            end_time=user_slot['end_time'])

