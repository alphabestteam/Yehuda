from django.urls import path
from . import views

urlpatterns = [
    path("users/AllUser/",views.all_user, name='AllUser' ),
    path("users/AddUser/",views.add_user, name='AddUser' ),
    path("users/delUser/<int:id>/",views.del_user, name='delUser' ),
    path("users/findUser/<int:id>/",views.find_user, name='findUser' ),
    path("users/changPasswordUser/",views.chang_password, name='changPasswordUser' ),
]