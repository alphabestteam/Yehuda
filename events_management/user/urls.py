from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.user_list, name='user-list'),
    path('add/', views.user_add, name='user-add'),
    path('delete/<int:pk>/', views.user_del, name='user-delete'),
    path('update/<int:pk>/', views.user_up, name='user-update'),
    path('find/<int:pk>/', views.user_find, name='user-detail'),
]