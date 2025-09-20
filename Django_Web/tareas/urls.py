from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_tareas, name='lista_tareas'),
    path('crear/', views.crear_tarea, name='crear_tarea'),
    path("editar/<int:tarea_id>/", views.editar_tarea, name="editar_tarea"),

    path('completar/<int:tarea_id>/', views.completar_tarea, name='completar_tarea'),
    path('eliminar/<int:tarea_id>/', views.eliminar_tarea, name='eliminar_tarea'),
    
    
        # Nuevas rutas de autenticación
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    
    path('perfil/', views.perfil, name='perfil'),
    
]   