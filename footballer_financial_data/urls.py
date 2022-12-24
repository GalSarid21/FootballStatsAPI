from django.urls import path
from . import views

urlpatterns = [
    path('ping/', views.ping),
    path('footballer/add/', views.add),
    path('footballer/all/', views.get_all),
    # footballer/by-net-worth supports query string with param: <bool: include-greaters>
    # example: footballer/by-net-worth/<int:net_worth>?include-greaters=false
    # default value = False (invalid values will be treated as default)
    path('footballer/by-net-worth/<int:net_worth>/', views.get_by_net_worth),
    path('footballer/<int:id>/update/', views.update),
    path('footballer/<int:id>/delete/', views.delete),
    path('footballer/<int:id>/', views.get),
    path('footballer/<str:full_name>/', views.get_by_full_name),
]
