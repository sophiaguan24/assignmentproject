from django.urls import path

from . import views

urlpatterns = [
    # path('', views.IndexView, name='index'),
    path('assignments/<username>',views.AssignmentView.as_view(),name='assignments'),
    path('assignments/<username>/make',views.MakeView.as_view(),name='make')
]
