from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path("Update/<int:pk>", views.Update_record, name='Update'),
    path("Delete/<int:pk>", views.DeleteRecord, name='Delete'),
    path("AddUser/", views.AddUser, name="AddUser"),
]




