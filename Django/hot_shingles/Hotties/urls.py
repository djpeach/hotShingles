from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'hotties'
urlpatterns = [
    path('', views.HottieListAll.as_view(), name='list_all_hotties'),
    path('<int:pk>/', views.HottieDetail.as_view(), name='detail_hottie'),
]