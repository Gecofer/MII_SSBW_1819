from django.urls import path

from . import views

urlpatterns = [

    # TAREA 1
    # --------------------------------------------------------------------------

    # Muestra 'hola' mundo en la raíz /hola_mundo
    # path('hola_mundo', views.hola_mundo), # entrada str

    # Es 'string' por defecto sino ponemos nada o 'str'
    # Si tiene una entrada se pone  'hola/<usuario>'
    path('hola/<usuario>', views.hola_mundo), # entrada str


    # TAREA 2
    # --------------------------------------------------------------------------

    # entrada str, lista separada por espacios, guiones o comas
    path('tarea2/ejercicio1/<lista>', views.tarea2_ejercicio1),

    # entrada str, lista separada por espacios, guiones o comas
    path('tarea2/ejercicio2/<lista>', views.tarea2_ejercicio2),

    # entrada str
    path('tarea2/ejercicio3/<entrada>', views.tarea2_ejercicio3),

    # entrada str
    path('tarea2/ejercicio4/<entrada>', views.tarea2_ejercicio4),

    # ninguna entrada, leemos un fichero en la función
    path('tarea2/ejercicio5', views.tarea2_ejercicio5),


    # TAREA 3
    # --------------------------------------------------------------------------

    # ninguna entrada
    path('tarea3/expresiones', views.ejercicio_expresiones_regulares),

    # ninguna entrada
    path('tarea3/titulares', views.extraer_titulares_imagenes),


    # TAREA 4
    # --------------------------------------------------------------------------

    # ninguna entrada
    path('tarea4/pymongo1', views.pymongo),

    # entrada del año de la película
    path('tarea4/pymongo2/<entrada>', views.pymongo_year),

    # entrada del actor de la película
    path('tarea4/pymongo3/<entrada>', views.pymongo_actor),

]
