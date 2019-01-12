from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'hotties'
urlpatterns = [
    path('', views.HottieListAll.as_view(), name='list_all_hotties'),
    path('<int:pk>/', views.HottieDetail.as_view(), name='detail_hottie'),
    path('register/', views.user_registration, name='registration'),
    path('login/', auth_views.LoginView.as_view(template_name='hotties/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='hotties/logout.html'), name='logout'),
    # path('profile/', views.user_profile, name='profile'),
]
