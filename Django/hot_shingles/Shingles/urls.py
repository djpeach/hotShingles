from django.urls import path, include
from . import views

app_name = 'shingles'
urlpatterns = [
    path('', views.ShingleListAll.as_view(), name='list_all_shingles'),
    path('<int:pk>/', views.ShingleDetail.as_view(), name='detail_shingle'),
    path('new/', views.ShingleCreate.as_view(), name='create_shingle'),
]