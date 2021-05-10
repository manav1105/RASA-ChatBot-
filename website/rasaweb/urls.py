from django.urls import path
from rasaweb import views

urlpatterns = [
    path('', views.index, name='index')
]