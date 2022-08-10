from django.urls import *
from . import views

urlpatterns = [
    path('', views.emailsend, name='emailsend'),
]