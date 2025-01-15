
from django.urls import path
from .import views


urlpatterns = [

path('', views.index),
path('harid', views.harid , name = 'harid'),
path('furush', views.furush , name = 'furush'),
path('test', views.test , name = 'test'),


]
