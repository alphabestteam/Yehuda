from django.urls import path
from random_num import views

urlpatterns = [
    path("getRandomNumber/", views.random_number, name="rand"),
    path("getRandomNumber/<number>", views.random_number_user, name="random_number_user"),
    path("getServerTime/", views.serverTime, name="ServerTime"),
    path("getLengthOfWord/<word>", views.LengthOfWord, name="LengthOfWord"),
    
]