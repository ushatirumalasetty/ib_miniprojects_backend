import factory
from slot_booking.models.user import User, WashingMachine, \
WashingMachineSlot, UserSlot, DaysRange, Request
import datetime


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Sequence(lambda n: "usha123%d" %n)
    last_name = factory.Sequence(lambda n: "tirumalasetty%d" %n)
    user_name = factory.Sequence(lambda n: "ushatirumalasetty%d" %n)
    role = "USER"

class WashingMachineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = WashingMachine

    washing_machine_id = factory.sequence(lambda n: "washing_machine_id%d" %n)
    status= "ACTIVE"

class WashingMachineSlotFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = WashingMachineSlot

    washing_machine = factory.SubFactory(WashingMachineFactory)
    start_time = datetime.time(8)
    end_time = datetime.time(9)
    day= "SUNDAY"


class UserSlotFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserSlot

    user = factory.SubFactory(User)
    washing_machine_slot = factory.SubFactory(WashingMachineFactory,
    washing_machine=factory.LazyAttribute(lambda o: o.factory_parent.washing_machine_slot))
    date = datetime.date(1996,12,22)
    start_time = datetime.time(6)
    end_time = datetime.time(7)


class DaysRangeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DaysRange

    days_range = 3


class RequestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Request

    requested_by = factory.SubFactory(User)
    date = factory.LazyFunction(datetime.date(1997,12,22))
    requested_user_slot = factory.SubFactory(UserSlot)
    request_status= "PENDING"
