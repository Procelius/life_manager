from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name


class Restriction(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name


class Goal(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    tasks = models.ManyToManyField(Task)
    restrictions = models.ManyToManyField(Restriction)

    def __str__(self):
        return self.name
