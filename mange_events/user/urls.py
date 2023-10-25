from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_user, name='add-user'),
    path('update/', views.update_user, name='update-user'),
    path('delete/<int:id>/', views.delete_user, name='delete-user'),
    path('all/', views.all_users, name='all-users'),
]