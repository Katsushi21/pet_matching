from django.db import models


class Dog_Data:
    """犬のデータ管理モデル"""
    GENDER = (('M', 'Male'), ('F', 'Female'))
    YES_OR_NO = (('1', 'Yes'), ('0', 'No'))

    name = models.CharField(max_length=30, verbose_name='name')
    gender = models.CharField(max_length=6, choices=GENDER, verbose_name='gender')
    age = models.PositiveIntegerField(verbose_name='age')
    height = models.PositiveIntegerField(verbose_name='height')
    observations = models.TextField(verbose_name='observations')
    energy_level = models.PositiveIntegerField(verbose_name='energy_level')
    people_friendly = models.PositiveIntegerField(verbose_name='people_friendly')
    dog_friendly = models.PositiveIntegerField(verbose_name='dog_friendly')
    color = models.CharField(max_length=20, verbose_name='color')
    hair = models.CharField(max_length=10, verbose_name='hair')
    reason_for_arrival = models.TextField(null=True, verbose_name='reason_for_arrival')
    walking_on_leash = models.CharField(max_length=3, choices=YES_OR_NO, verbose_name='walking_on_leash')
    can_live_with_dogs = models.CharField(max_length=3, choices=YES_OR_NO, verbose_name='can_live_with_dogs')
