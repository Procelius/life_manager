'''
urls for schedule
'''

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^schedule_builder/$', views.schedule_builder, name='schedule_builder'),
]
