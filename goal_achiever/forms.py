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
