from django.shortcuts import render
from goal_achiever.models import Task


def schedule_builder(request):
    '''
    docstring
    '''
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, 'schedule/schedule_builder.html', context)
