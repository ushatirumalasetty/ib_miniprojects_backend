from covid_dashboard.models import *    
import factory

'''

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    name = "John Doe"

class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Group

    name = "Admins"

class GroupLevelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GroupLevel

    user = factory.SubFactory(UserFactory)
    group = factory.SubFactory(GroupFactory)
    rank = 1

class UserWithGroupFactory(UserFactory):
    membership = factory.RelatedFactory(GroupLevelFactory, 'user')

class UserWith2GroupsFactory(UserFactory):
    membership1 = factory.RelatedFactory(GroupLevelFactory, 'user', group__name='Group1')
    membership2 = factory.RelatedFactory(GroupLevelFactory, 'user', group__name='Group2')
    '''
    # factories.py

class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country

    name = factory.Iterator(["France", "Italy", "Spain"])
    lang = factory.Iterator(['fr', 'it', 'es'])

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    name = "John"
    lang = factory.SelfAttribute('country.lang')
    country = factory.SubFactory(CountryFactory)

class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    name = "ACME, Inc."
    country = factory.SubFactory(CountryFactory)
    owner = factory.SubFactory(UserFactory, country=factory.SelfAttribute('..country'))


# factories.py
class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person

    log = factory.RelatedFactory(UserLogFactory, 'person', action=UserLog.ACTION_CREATE)