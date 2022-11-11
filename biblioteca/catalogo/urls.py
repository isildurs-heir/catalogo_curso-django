from django.urls import path, include
from catalogo import views

urlpatterns = [
    path('',views.index, name='index')
]