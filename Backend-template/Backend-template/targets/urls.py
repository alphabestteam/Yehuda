from django.urls import path
from . import views

urlpatterns = [
    # Add here all the URLs you need
    path("AddTarget/",views.add_target, name='target' ),
    path("AllTargets/",views.all_targets, name='target' ),

]
