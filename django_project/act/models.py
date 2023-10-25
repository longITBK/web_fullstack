# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Uni(models.Model):
    name = models.CharField(max_length=90, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)


class Student(models.Model):
    uni = models.ForeignKey(Uni, on_delete=models.CASCADE)
    name = models.CharField(max_length=90, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

class Building(models.Model):
    name = models.CharField(max_length=90, blank=True, null=True)
    

class Room(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    FLOORS = [
        ('1', 'First floor'),
        ('2', 'Second floor'),
        ('3', 'Third floor'),
        ('4', 'Fourth floor'),
        ('5', 'Fifth floor'),
    ]
    floor = models.CharField(max_length=2, choices=FLOORS, null=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

class Topping(models.Model):
    name = models.CharField(max_length=90, null=True, blank=True)

class Pizza(models.Model):
    name = models.CharField(max_length=90, null=True, blank=True)
    Toppings = models.ManyToManyField(Topping)

class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    # members = models.ManyToManyField(Person, through="Membership")

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)