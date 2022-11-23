from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('params',views.getParams,name='params')
]