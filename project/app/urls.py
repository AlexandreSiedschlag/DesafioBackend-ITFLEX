from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('list/', views.List, name='List'),
    path('detail/<str:pk>/', views.List, name='Detail'),
    path('create/', views.Create, name='Create'),
    path('update/<str:pk>/', views.Update, name='Update'),
    path('delete/<str:pk>/', views.Delete, name='Delete'),
]
