# -*- coding: utf-8 -*-
from django.conf.urls import url
from myproject.myapp.views import list
from myproject.myapp.views import devices
from myproject.myapp.views import createRun
from myproject.myapp.views import browseiosdevices

urlpatterns = [
    url(r'^list/$', list, name='list'),
    url(r'^devices/$', devices, name='devices'),
    url(r'^createrun/$', createRun, name='createRun'),
    url(r'^viewiOSList/$', browseiosdevices, name='browseiosdevices')

]
