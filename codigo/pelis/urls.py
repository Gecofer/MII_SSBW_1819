from django.urls import path
from django.conf.urls import include, url
from rest_framework import routers
from . import views
from .viewsets import PelisViewSet

router = routers.DefaultRouter()
router.register('pelis', PelisViewSet, 'peli')

urlpatterns = [

    # PAGINA INICIO PARA BUSCADOR
    # --------------------------------------------------------------------------

    # entrada del actor de la película
    path('buscador', views.buscador, name="buscador"),


    # TAREA 4
    # --------------------------------------------------------------------------

    # entrada del actor de la película
    path('tarea4/mongoengine1/<entrada>', views.mongoengine_year),


    # TAREA 5
    # --------------------------------------------------------------------------

    # entrada del actor de la película
    path('pelis_que_sale/<entrada>', views.pelis_que_sale, name="pelis_que_sale"),

    # ninguna entrada
    path('formulario', views.formulario, name= "formulario"),

    # ninguna entrada
    path('peliculas_actor', views.peliculas_actor),


    # TAREA 6
    # --------------------------------------------------------------------------

    # ninguna entrada
    path('formulario_id', views.formulario_id, name= "formulario_id"),

    # ninguna entrada
    path('peliculas_id', views.peliculas_id),

    # entrada el ID de la película
    path('informacion_pelicula/<id>', views.informacion_pelicula, name="informacion_pelicula"),


    # TAREA 7
    # --------------------------------------------------------------------------

    # ninguna entrada
    path('crud', views.crud, name="crud"),

    # ninguna entrada
	path('crear_pelicula', views.crear_pelicula),

    # entrada el ID de la película
	path('editar_pelicula/<id>', views.editar_pelicula),

    # entrada el ID de la película
	path('borrar_pelicula/<id>', views.borrar_pelicula),


    # TAREA 12
    # --------------------------------------------------------------------------

    # ninguna entrada
    # GET lista todas, POST añade
    path('api_pelis',    views.api_pelis, name="api_pelis"),

    # entrada del ID de la película
    # GET lista una,   PUT modifica, DELETE borrra
    path('api_peli/<id>', views.api_peli, name="api_peli"),

    # se tiene que llamar con la URL
    url('api', include(router.urls))
]
