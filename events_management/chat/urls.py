from django.urls import path
from . import views

urlpatterns = [ 
    path('all/', views.event_chat_list, name='event-chat-list'),
    path('add/', views.event_chat_add, name='event-chat-add'),
    path('delete/<int:pk>/', views.event_chat_del, name='event-chat-delete'),
    
    path('message/all/', views.event_message_list, name='event-message-list'),
    path('message/add/', views.event_message_add, name='event-message-add'),
    path('message/delete/<int:pk>/', views.event_message_del, name='event-message-delete'),          
    path('message/update/<int:pk>/', views.event_message_up, name='event-chat-update'),
    path('message/find/<int:pk>/', views.event_message_find, name='event-chat-detail'),
               
]