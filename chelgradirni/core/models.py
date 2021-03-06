# -*- coding: utf8 -*-

from django.db import models
from photologue.models import Gallery, Photo

# Create your models here.

class Cooler(models.Model):
    name = models.CharField(u'Название', blank=True, max_length=10)
    performance = models.CharField(u'Производительность', blank=True, max_length=5)
    load = models.CharField(u'Тепловая нагрузка', blank=True, max_length=5)
    drop = models.CharField(u'Перепад температур', blank=True, max_length=5)
    power = models.CharField(u'Мощность вентелятора', blank=True, max_length=5)
    weight = models.CharField(u'Масса', blank=True, max_length=5)
    dimension = models.CharField(u'Габаритные размеры', blank=True, max_length=15)
    
    photo = models.ForeignKey(Photo, verbose_name=u'Изображение ГВП', blank=True, null=True)
#     schema = models.ForeignKey(Photo, verbose_name=u'Схема ГВП', blank=True, null=True)
    