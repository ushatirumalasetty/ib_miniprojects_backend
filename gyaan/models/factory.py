import factory
from datetime import datetime, timedelta, date
from factory import fuzzy

class User():
    def __init__(self, username:str, name:str, email:str):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return "{} {}".format(self.username,self.name)


class Log():
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "{} {}".format(self.start_time,self.end_time)

class Order():
    def __init__(self, status, shipped_by, shipped_on):
        self.status = status
        self.shipped_by = shipped_by
        self.shipped_on = shipped_on
    
    def __repr__(self):
        return "{}".format(self.status)


class UserFactory(factory.Factory):
    class Meta:
        model = User

    name = "usha"

    @factory.sequence
    def username(n):
        return "user%d" % n

    email = factory.LazyAttribute(lambda obj: '%s@example.com' %obj.username)


class LogFactory(factory.Factory):
    class Meta:
        model = Log

    start_time = factory.fuzzy.FuzzyDate(start_date=date.today()+timedelta(days=-1))
    end_time = factory.LazyAttribute(lambda o: o.start_time + timedelta(days=o.duration+o.value))

    class Params:
        duration = 12
        value=1
class OrderFactory(factory.Factory):
    status = "pending"
    shipped_by = None
    shipped_on = None
    
    class Meta:
        model = Order
        
    class Params:
        shipped = factory.Trait(
            status = "shipped",
            shipped_by = factory.SubFactory(UserFactory),
            shipped_on = factory.LazyFunction(date.today),
            )


    
class Account:
        def __init__(self,username, email, date_joined):
            self.username = username
            self.email = email
            self.date_joined = date_joined
        
        def __str__(self):
            return "%s (%s)" % (self.username, self.email)
            
    
class Profile:
        
        GENDER_MALE = 'm'
        GENDER_FEMALE  = 'f'
        GENDER_UNKNOWN = 'u'
        
        def __init__(self, account, gender, firstname, lastname, plannet):
            self.account = account
            self.gender = gender
            self.firstname = firstname
            self.lastname = lastname
            self.plannet = plannet
        
        def __str__(self):
            return "%s %s (%s)" % (self.firstname, self.lastname, self.account.username)
            
            
import datetime 
import factory
import random



class AccountFactory(factory.Factory):
    class Meta:
        model = Account
        
    username = factory.Sequence(lambda n: "usha%s" % n)
    email = factory.LazyAttribute(lambda o: "%s@example.org" % o.username)
    date_joined = factory.LazyFunction(datetime.datetime.now)
    
    
class ProfileFactory(factory.Factory):
    class Meta:
        model = Profile
    
    account = factory.SubFactory(AccountFactory)
    gender = factory.Iterator([Profile.GENDER_FEMALE,Profile.GENDER_UNKNOWN,Profile.GENDER_MALE])
    firstname = "usha"
    lastname = "tirumalasetty"
    
class FemaleProfileFactory(ProfileFactory):
    gender = Profile.GENDER_FEMALE
    firstname = "usha"
    account__username = factory.Sequence(lambda n: "jane%s" % n )
    
    

    
    
    