from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('allfinches/', views.finches, name='allfinches'),
    path('finches/finchdetail/<int:finch_id>', views.finchdetail, name='finchdetail'),
    path('create/', views.create.as_view(), name='create'),
    path('finchdetail/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
    path('finchdetail/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('finchdetail/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('finchdetail/<int:finch_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy')
]
