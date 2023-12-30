from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login-user"),
    path('logout/', views.logoutUser, name="logout-user"),
    path('register/', views.registerPage, name="register-user"),
    path('', views.home, name="home"),
    path("create-room/", views.createRoom, name="create-room"),
    path('room/<str:pk>/', views.room, name="room"),
    path("update-room/<str:pk>", views.updateRoom, name="update-room"),
    path("delete-room/<str:pk>", views.deleteRoom, name="delete-room")
]
