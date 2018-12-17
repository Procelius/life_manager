from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^goal_list/$', views.goal_list, name='goal_list'),
    url(r'^goal_list/(?P<goal_id>[0-9]+)/$', views.goal, name='goal'),

    url(r'^task_list/$', views.task_list, name='task_list'),
    url(r'^task_list/(?P<task_id>[0-9]+)/$', views.task, name='task'),

    url(r'^restriction_list/$',
        views.restriction_list,
        name='restriction_list'
    ),
    url(r'^restriction_list/(?P<restriction_id>[0-9]+)/$',
        views.restriction,
        name='restriction'
    ),
]
