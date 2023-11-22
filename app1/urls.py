from django.urls import path
from app1.views import *
app_name='anything'
urlpatterns=[
    path('p1/', p1, name='p1'),
]