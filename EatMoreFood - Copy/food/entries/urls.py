from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.add, name='add'),
    path('past/', views.past, name='past'),
    path('new/', views.new, name='new'),
]
