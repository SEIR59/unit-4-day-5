from django.urls import path
from . import views

urlpatterns = [
  # root route localhost:8000/
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('cats/', views.cats_index, name='index'),
]