from django.urls import path
from . import views

urlpatterns = [
    # Add here all the URLs you need
    path("AddTarget/",views.add_target, name='AddTarget' ),
    path("AllTargets/",views.all_targets, name='AllTargets' ),
    path("UpdateTarget/",views.update_target, name='UpdateTarget' ),

]
