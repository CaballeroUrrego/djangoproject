from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,),
    path('about/', views.about, ),
    path('inicio/<str:username>/', views.inicio),  # Cambié usurname por username para que coincida
]