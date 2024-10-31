
# URL configuration for bookmodule (Tasks 1, 3, 6, and 7)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # Task 1: index view
    path('index2/<int:val1>/', views.index2),  # Task 3: index2 view with parameter
    path('<int:bookId>/', views.viewbook),  # Task 7: viewbook detail view with bookId parameter
]
