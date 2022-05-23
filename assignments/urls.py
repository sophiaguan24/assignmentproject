from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('assignments/<username>',views.AssignmentView.as_view(),name='assignments'),
    path('profile/<username>',views.ProfileView.as_view(),name='profile'),
    path('assignments/<username>/make',views.MakeView.as_view(),name='make'),
    path('profile/<username>/edit',views.EditView.as_view(),name='edit'),
    path('profile/<username>/create',views.CreateView.as_view(),name='create'),
]
