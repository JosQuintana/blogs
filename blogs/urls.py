from django.urls import path     
from . import views

#parte con /
urlpatterns = [
    path('respuesta', views.index),	 
    path('blogs', views.root),
    path('', views.redirige),
    path('blogs/new', views.new),
    path('blogs/<int:numero>/edit',views.edit),
]