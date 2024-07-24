from django.urls import path
from .views import studentz,studentttt
urlpatterns = [
    path('index',studentz,name='index'),
    path('home/<pk>',studentttt,name='home')
]
