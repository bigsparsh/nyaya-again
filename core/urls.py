from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('user_register/', views.user_register, name="user_register"),
    path('lawyer_register/', views.lawyer_register, name="lawyer_register"),
    path('query_generator/', views.query_generator, name="query_generator"),
    path('info_page/', views.info_page, name="info_page"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('logout/', views.logout, name="logout"),
    path('clear_buffer/', views.clear_buffer, name="clear_buffer"),
    path('query_accept/', views.query_accept, name="query_accept"),
]