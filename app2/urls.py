from django.urls import path
from app2.views import *
app_name='nothing'
urlpatterns=[
    path('p2/', p2, name='p2'),
]