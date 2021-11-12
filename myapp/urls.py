from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name ="home_page"),
    path('details/<int:id>', views.details, name = "details"),
    path('admin/',views.admin, name="admin"),
    
]