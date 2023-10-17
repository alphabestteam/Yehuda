from django.urls import path
from . import views

urlpatterns = [
    path("people/AddPeople/",views.add_people, name='AddTarget' ),
    path("people/delPeople/<int:id>/",views.del_people, name='AllTargets' ),
    path("people/UpdatePeople/",views.update_people, name='UpdateTarget' ),
]