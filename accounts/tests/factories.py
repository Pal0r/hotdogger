import factory

from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@hotdogger.com")
    is_active = True


class AuthTokenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Token
