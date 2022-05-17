from django.urls import path

from . import views

urlpatterns = [
    # path('', views.IndexView, name='index'),
    path('assignments',views.assignmentView.as_view(),name='assignments')
    # path('assignments',views.AssignmentView,name='assignment')
]
