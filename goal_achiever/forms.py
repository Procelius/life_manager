'''
forms for createing new goals, tasks and restrictions
'''

from django import forms

from . import models


class NewGoalForm(forms.ModelForm):
    '''
    a form for creating new goals
    '''
    class Meta:
        model = models.Goal
        fields = ('name',
                  'description')


class NewTaskForm(forms.ModelForm):
    '''
    a form for creating new tasks
    '''
    class Meta:
        model = models.Task
        fields = ('name',
                  'description')


class NewRestrictionForm(forms.ModelForm):
    '''
    a form for creating new restrictions
    '''
    class Meta:
        model = models.Restriction
        fields = ('name',
                  'description')
