from django.shortcuts import render, get_object_or_404

from .models import Goal, Restriction, Task


def goal(request, goal_id):
    goal = get_object_or_404(Goal, pk=goal_id)
    context = {
        'goal': goal,
    }
    return render(request, 'goal_achiever/goal.html', context)


def goal_list(request):
    goals = Goal.objects.all()
    context = {
        'goals': goals,
    }
    return render(request, 'goal_achiever/goal_list.html', context)


def task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task_goals = task.goal_set.all()
    context = {
        'task': task,
        'task_goals': task_goals,
    }
    return render(request, 'goal_achiever/task.html', context)


def task_list(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, 'goal_achiever/task_list.html', context)


def restriction(request, restriction_id):
    restriction = get_object_or_404(Restriction, pk=restriction_id)
    restriction_goals = restriction.goal_set.all()
    context = {
        'restriction': restriction,
        'restriction_goals': restriction_goals,
    }
    return render(request, 'goal_achiever/restriction.html', context)


def restriction_list(request):
    restrictions = Restriction.objects.all()
    context = {
        'restrictions': restrictions,
    }
    return render(request, 'goal_achiever/restriction_list.html', context)
