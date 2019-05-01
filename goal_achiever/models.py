'''
goal_achiever models
'''

from django.db import models


class Task(models.Model):
    '''
    a Task model
    '''
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name


class Restriction(models.Model):
    '''
    a Restriction model
    '''
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name


class Goal(models.Model):
    '''
    a Goal model
    '''
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    tasks = models.ManyToManyField(Task, blank=True)
    restrictions = models.ManyToManyField(Restriction, blank=True)

    def __str__(self):
        return self.name
