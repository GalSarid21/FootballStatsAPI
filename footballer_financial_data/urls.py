from django.urls import path
from . import views

urlpatterns = [
    path('ping/', views.ping),
    path('footballer/add/', views.add),
    path('footballer/all/', views.get_all),
    path('footballer/<int:id>/', views.get),
    path('footballer/<str:full_name>/', views.get_by_full_name),
]
