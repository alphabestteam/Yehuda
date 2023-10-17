from django.urls import path
from . import views

urlpatterns = [
    path("people/AllPeople/",views.all_people, name='AllPeople' ),
    path("people/AddPeople/",views.add_people, name='AddPeople' ),
    path("people/delPeople/<int:id>/",views.del_people, name='delPeople' ),
    path("people/UpdatePeople/",views.update_people, name='UpdatePeople' ),
    
    path("people/AllParent/",views.all_parent, name='AllParent' ),
    path("people/AddParent/",views.add_parent, name='AddParent' ),
    path("people/delParent/<int:id>/",views.del_parent, name='delParent' ),
    path("people/UpdateParent/",views.update_parent, name='UpdateParent' ),
    path("people/ConnectChild/",views.Connect_Child_Parent, name='UpdateParent'),
    path("people/ParentAndChild/",views.parent_and_child, name='ParentAndChild' ),
    path("people/richKid/",views.rich_kid, name='richKid' ),
    path("people/findParent/<int:id>/",views.find_parent, name='findParent' ),
    path("people/findSon/<int:id>/",views.find_son, name='findSon' ),
    path("people/findGrandfather/<int:id>/",views.find_grandfather, name='findGrandfather' ),
    path("people/findSiblings/<int:id>/",views.find_Siblings, name='findSiblings' ),

    
]