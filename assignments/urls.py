from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('assignments/<username>',views.AssignmentView.as_view(),name='assignments'),
    path('profile/<username>',views.ProfileView.as_view(),name='profile'),
    path('assignments/<username>/make',views.MakeView.as_view(),name='make'),
    path('assignments/<username>/edit',views.EditAssignView.as_view(),name='editassignment'),
    path('profile/<username>/edit',views.EditView.as_view(),name='edit'),
    path('assignments/<username>/edit/delete',views.DeleteView.as_view(),name='delete'),
    path('profile/<username>/edit/save',views.SaveEditView.as_view(),name='save'),
    path('profile/<username>/create',views.CreateView.as_view(),name='create'),
]
