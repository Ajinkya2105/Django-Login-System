from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='login'),
    path('sign_up/', views.signup, name='signup'),
]
