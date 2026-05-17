from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_musica, name='lista_musica'),
    path('agregar/', views.agregar_cancion, name='agregar_cancion'),
    path('cancion/<int:cancion_id>/', views.detalle_cancion, name='detalle_cancion'),
    path('api/canciones/', views.api_canciones, name='api_canciones'),
]