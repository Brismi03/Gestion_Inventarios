from django.urls import path
from generales.views import home
from .views import login_view

urlpatterns=[
    path('', login_view, name='login'),
    path('dashboard/', home, name='home')
]