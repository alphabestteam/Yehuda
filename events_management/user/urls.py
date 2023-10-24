from django.urls import path
from . import views
 
urlpatterns = [
    path('create/', views.add_user, name='add-user'),
    path('all/', views.view_user, name='view_user'),
    path('update/<int:pk>/', views.update_user, name='update-user'),
    path('<int:pk>/delete/', views.delete_user, name='delete-user'),

]