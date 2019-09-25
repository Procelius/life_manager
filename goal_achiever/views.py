'''
goal_achiever views
'''

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Goal, Restriction, Task
from .forms import NewGoalForm, NewTaskForm, NewRestrictionForm


def goal(request, goal_id):
    '''
    docstring
    '''
    selected_goal = get_object_or_404(Goal, pk=goal_id)
    context = {
        'goal': selected_goal,
    }
    return render(request, 'goal_achiever/goal.html', context)


def add_delete_items(request):
    '''
    save goal list changes
    '''
    if request.method == "POST":
        data = request.POST.copy()
        control = data['control']
        active_class = None
        num_of_items_to_create = int(data['Q'])
        items_to_delete = data.getlist('D[]')
        num_of_items_to_delete = len(items_to_delete)

        try:
            active_item = get_object_or_404(Goal, pk=data['item_pk'])
        except Exception:
            pass

        if control == 'goals':
            active_class = Goal
        elif control == 'tasks':
            active_class = Task
        elif control == 'restrictions':
            active_class = Restriction
        else:
            return JsonResponse({'response': 'error: invalid form control'})

        # create items
        i = 0
        while i is not num_of_items_to_create:
            create_item = {
                'name': data['C[{}][name]'.format(i)],
                'description': data['C[{}][description]'.format(i)],
            }
            if control == 'goals':
                form = NewGoalForm(create_item)
                form.save()
            elif control == 'tasks':
                form = NewTaskForm(create_item)
                form.save()
                active_item.tasks.add(Task.objects.last().pk)
            elif control == 'restrictions':
                form = NewRestrictionForm(create_item)
                form.save()
                active_item.restrictions.add(Restriction.objects.last().pk)

            i = i + 1

        # delete items
        i = 0
        while i is not num_of_items_to_delete:
            instance = get_object_or_404(active_class,
                                         pk=int(items_to_delete[i]))
            instance.delete()
            i = i + 1

        return JsonResponse({'response': 'success'})
    else:
        return JsonResponse({'response': 'error: wrong request'})


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
