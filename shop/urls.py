from django.urls import path
from . import views

add_name='shop'

urlpatterns=[
	path('', views.index, name='index'),
]