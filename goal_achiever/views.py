'''
goal_achiever views
'''

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect

from .models import Goal, Restriction, Task
from .forms import NewGoalForm


def goal(request, goal_id):
    '''
    docstring
    '''
    selected_goal = get_object_or_404(Goal, pk=goal_id)
    context = {
        'goal': selected_goal,
    }
    return render(request, 'goal_achiever/goal.html', context)


def goal_delete(request, goal_id):
    '''
    docstring
    '''
    if request.method == "POST":
        instance = get_object_or_404(Goal, pk=goal_id)
        instance.delete()
    return JsonResponse({})


def goal_list(request):
    '''
    docstring
    '''
    if request.method == "POST":
        form = NewGoalForm(request.POST)
        if form.is_valid():
            form.save()
            form = NewGoalForm()
            return HttpResponseRedirect('./')
    else:
        form = NewGoalForm()

    goals = Goal.objects.all()
    context = {
        'goals': goals,
        'form': form,
    }
    return render(request, 'goal_achiever/goal_list.html', context)


def task(request, task_id):
    '''
    docstring
    '''
    selected_task = get_object_or_404(Task, pk=task_id)
    task_goals = selected_task.goal_set.all()
    context = {
        'task': selected_task,
        'task_goals': task_goals,
    }
    return render(request, 'goal_achiever/task.html', context)


def task_list(request):
    '''
    docstring
    '''
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, 'goal_achiever/task_list.html', context)


def restriction(request, restriction_id):
    '''
    docstring
    '''
    selected_restriction = get_object_or_404(Restriction, pk=restriction_id)
    restriction_goals = selected_restriction.goal_set.all()
    context = {
        'restriction': selected_restriction,
        'restriction_goals': restriction_goals,
    }
    return render(request, 'goal_achiever/restriction.html', context)


def restriction_list(request):
    '''
    docstring
    '''
    restrictions = Restriction.objects.all()
    context = {
        'restrictions': restrictions,
    }
    return render(request, 'goal_achiever/restriction_list.html', context)
