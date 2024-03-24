from django.urls import path
from users import views



urlpatterns = [

    path('', views.users, name='users'),
    path('cache/clear/', views.cache_clear, name='cache_clear'),
    path('cache/clear/users/', views.cache_clear_users, name='cache_clear_users'),

]