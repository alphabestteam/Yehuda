from django.urls import path
from . import views

urlpatterns = [
    path("people/AllPeople/",views.all_people, name='AllPeople' ),
    path("people/AddPeople/",views.add_people, name='AddPeople' ),
    path("people/delPeople/<int:id>/",views.del_people, name='delPeople' ),
    path("people/UpdatePeople/",views.update_people, name='UpdatePeople' ),
]