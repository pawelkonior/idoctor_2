from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class Nationality(models.Model):
    iso = models.CharField(max_length=2)
    full_name = models.CharField(max_length=56)


class QueuePriority(models.Model):
    name = models.CharField(max_length=30)
    level = models.IntegerField(default=0, help_text="Higher is more important. Add levels with big tiers.")


class Address(models.Model):
    street = models.CharField(max_length=50)
    building_number = models.CharField(max_length=5)
    flat_number = models.CharField(max_length=5, blank=True, null=True)
    zip_code = models.CharField(max_length=6)
    city = models.CharField(max_length=85)
    country = models.CharField(max_length=56)
    address_type = models.IntegerChoices('Address', 'address correspondence billing registered shipping')


class Specialization(models.Model):
    specialization = models.CharField(max_length=50)


class CustomUser(AbstractUser):
    class GenderType(models.IntegerChoices):
        MALE = 1
        FEMALE = 2
        RATHER_NOT_SAY = 3

    personal_identity_number = models.CharField(max_length=50)
    nationality = models.ForeignKey('Nationality', on_delete=models.DO_NOTHING, related_name='users')
    birthday = models.DateField()
    gender = models.IntegerField(choices=GenderType.choices)
    is_doctor = models.BooleanField(default=False)
    queue_priority = models.ForeignKey('QueuePriority', default=1,
                                       on_delete=models.SET_DEFAULT, related_name='users')
    address = models.ManyToManyField('Address', related_name='user_address', through='CustomUserAddress')
    specialization = models.ManyToManyField('Specialization', blank=True)


class CustomUserAddress(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), related_name='user_address', on_delete=models.DO_NOTHING)
    address = models.ForeignKey('Address', related_name='address_user', on_delete=models.DO_NOTHING)
