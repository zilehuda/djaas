import factory
from factory.django import DjangoModelFactory
from apps.users import models


class UserFactory(DjangoModelFactory):
    class Meta:
        model = models.User

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    username = factory.Faker("email")
    email = factory.sequence(lambda n: "test{}@example.com".format(n))
    password = factory.PostGenerationMethodCall("set_password", "secret_pwd")
    is_staff = False
    is_superuser = False
