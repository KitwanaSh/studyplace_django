from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login-user"),
    path('logout/', views.logoutUser, name="logout-user"),
    path('register/', views.registerPage, name="register-user"),
    path('', views.home, name="home"),
    path("create-room/", views.createRoom, name="create-room"),
    path('room/<str:pk>/', views.room, name="room"),
    path('user-profile/<str:pk>/', views.Profile, name="user-profile"),

    path("update-room/<str:pk>", views.updateRoom, name="update-room"),
    path("delete-room/<str:pk>", views.deleteRoom, name="delete-room"),
    path("delete-message/<str:pk>", views.deleteMessage, name="delete-message"),

    path("update-user/", views.updateUser, name="update-user"),

    path("topics/", views.topicsPage, name="topics")
]
