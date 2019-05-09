from django.urls import path
from . import views

urlpatterns = [
    path('', views.dive_list, name='dive_list'),
    path('dive/<int:pk>/', views.dive_detail, name='dive_detail'),
    path('profile/', views.profile, name='profile'),
    path('dive/new/', views.dive_new, name='dive_new'),
    path('dive/<int:pk>/delete/', views.dive_delete, name='dive_delete'),
]
