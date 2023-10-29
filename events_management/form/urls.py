from django.urls import path
from . import views

urlpatterns = [
    path('regular/all/', views.event_list, name='event-list'),
    path('regular/add/', views.event_add, name='event-add'),
    path('regular/delete/<int:pk>/', views.event_del, name='event-delete'),
    path('regular/update/<int:pk>/', views.event_up, name='event-update'),
    path('regular/find/<int:pk>/', views.event_find, name='event-detail'),
    
    path('file/all/', views.event_file_list, name='event-file-list'),
    path('file/add/', views.event_file_add, name='event-file-add'),
    path('file/delete/<int:pk>/', views.event_file_del, name='event-file-delete'),
    path('file/update/<int:pk>/', views.event_file_up, name='event-file-update'),
    path('file/find/<int:pk>/', views.event_file_find, name='event-file-detail'),
]