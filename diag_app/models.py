from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Tech(models.Model):
    experience = models.IntegerField(default=0)
    job_title = models.CharField(null=True, max_length=25)
    shop = models.CharField(null=True, max_length=25)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tech')
    tech_rating = models.IntegerField(default=0)

    @receiver(post_save, sender=User)
    def create_tech_profile(self, sender, instance, created, **kwargs):
        if created:
            Tech.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_tech_profile(self, sender, instance, **kwargs):
        instance.tech.save()

    class JSONAPIMeta:
        resource_name = "techs"


class Brand(models.Model):
    name = models.CharField(max_length=40)
    make_id = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)


class Year(models.Model):
    value = models.CharField(max_length=4)

    def __str__(self):
        return str(self.value)


class Model(models.Model):
    name = models.CharField(max_length=40)
    brand = models.ForeignKey(Brand)
    year = models.ForeignKey(Year)


    class JSONAPIMeta:
        resource_name = "models"

    def __str__(self):
        return str(self.name)


class Problem(models.Model):
    title = models.CharField(max_length=65)
    system = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    tech = models.ForeignKey(Tech)
    model = models.ForeignKey(Model, related_name='problems')
    posted = models.DateTimeField(auto_now=True)
    mileage = models.IntegerField(default=0)

    def __str__(self):
        return str(self.title)

    class JSONAPIMeta:
        resource_name = "problems"




class Solution(models.Model):
    description = models.TextField(max_length=500)
    time_required = models.FloatField(default=0)
    parts_cost = models.DecimalField(max_digits=6, decimal_places=2)
    problem = models.ForeignKey(Problem, related_name='solutions')
    tech = models.ForeignKey(Tech)
    posted = models.DateTimeField(auto_now=True)
    score = models.IntegerField(default=0)

    class JSONAPIMeta:
        resource_name = "solutions"


class Commit(models.Model):
    solution = models.ForeignKey(Solution)
    tech = models.ForeignKey(Tech)
    posted = models.DateTimeField(auto_now=True)
    text = models.TextField(max_length=500)

    class JSONAPIMeta:
        resource_name = "commits"


class Notification(models.Model):
    tech = models.ForeignKey(Tech)
    message = models.CharField(max_length=20)
    solution = models.ForeignKey(Solution, null=True)
    commit = models.ForeignKey(Commit, null=True)
    posted = models.DateTimeField(auto_now=True)

    class JSONAPIMeta:
        resource_name = "notifications"
