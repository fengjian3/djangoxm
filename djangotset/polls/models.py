from django.db import models


# Create your models here.


class Depot1(models.Model):
    iname = models.IntegerField(primary_key=True)
    cname = models.CharField(max_length=32)
    number = models.IntegerField()


class Depot2(models.Model):
    iname = models.IntegerField(primary_key=True)
    cname = models.CharField(max_length=32)
    number = models.IntegerField()


class Depot3(models.Model):
    iname = models.IntegerField(primary_key=True)
    cname = models.CharField(max_length=32)
    number = models.IntegerField()


class cargo(models.Model):
    iname = models.IntegerField(primary_key=True)
    cname = models.CharField(max_length=32)
    number = models.IntegerField()
    site = models.CharField(max_length=255)


class user(models.Model):
    iname = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    pwd = models.IntegerField()
