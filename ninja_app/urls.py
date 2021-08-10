from django.urls import path
from . import views	

urlpatterns = [
    path('', views.index),
    path('getmoney/<name>', views.getmoney),
    path('reset', views.reset),
]