from app1.views import *
from django.urls import path

app_name='app1'
urlpatterns=[
    path('isharani/',isharani,name='isharani')
]