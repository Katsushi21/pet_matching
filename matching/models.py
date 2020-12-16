from django.db import models


class Dog_Data:
    """犬のデータ管理モデル"""
    GENDER = (('M', 'Male'), ('F', 'Female'))
    YES_OR_NO = (('1', 'Yes'), ('0', 'No'))

    name = models.CharField(max_length=30, verbose_name='Name')
    gender = models.CharField(max_length=6, choices=GENDER, verbose_name='Gender')
    age = models.PositiveIntegerField(verbose_name='Age')
    height = models.PositiveIntegerField(verbose_name='Height')
    observations = models.TextField(verbose_name='Observations')
    energy_level = models.PositiveIntegerField(verbose_name='Energy level')
    people_friendly = models.PositiveIntegerField(verbose_name='People friendly')
    dog_friendly = models.PositiveIntegerField(verbose_name='Dog friendly')
    color = models.CharField(max_length=20, verbose_name='Color')
    hair = models.CharField(max_length=10, verbose_name='Hair')
    reason_for_arrival = models.TextField(null=True, verbose_name='Reason for arrival')
    walking_on_leash = models.CharField(max_length=3, choices=YES_OR_NO, verbose_name='Walking on leash')
    can_live_with_dogs = models.CharField(max_length=3, choices=YES_OR_NO, verbose_name='Can live with dogs')
