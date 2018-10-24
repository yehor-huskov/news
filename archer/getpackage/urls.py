from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from getpackage import views

urlpatterns = [
    path('news/', views.PostApproved.as_view()),
    path('posts/', views.PostAll.as_view()),
    path('posts/<int:pk>/', views.PostOne.as_view()),
    path('users/', views.UserAll.as_view()),
    path('users/<int:pk>/', views.UserOne.as_view()),
]

