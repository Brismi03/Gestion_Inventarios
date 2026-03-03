from django.urls import path
from generales.views import home

urlpatterns=[
    path('', home, name='home')
]