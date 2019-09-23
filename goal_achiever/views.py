'''
goal_achiever views
'''

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

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


def save_goal_list(request):
    '''
    save goal list changes
    '''
    # TODO: separate create, delete and del csrf
    if request.method == "POST":
        data = request.POST.copy()
        num_of_goals_to_create = int(data['Q'])
        goals_to_delete = data.getlist('D[]')
        num_of_goals_to_delete = len(goals_to_delete)
        # create goals
        i = 0
        while i is not num_of_goals_to_create:
            create_goal = {
                'name': data['C[{}][name]'.format(i)],
                'description': data['C[{}][description]'.format(i)]
            }
            form = NewGoalForm(create_goal)
            form.save()
            i = i + 1

        # delete goals
        i = 0
        while i is not num_of_goals_to_delete:
            instance = get_object_or_404(Goal, pk=int(goals_to_delete[i]))
            instance.delete()
            i = i + 1

        return JsonResponse({'response': 'cleaned_data'})
    else:
        return JsonResponse({'response': 'error'})


def goal_list(request):
    '''
    docstring
    '''
    goals = Goal.objects.all()
    context = {
        'goals': goals,
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
