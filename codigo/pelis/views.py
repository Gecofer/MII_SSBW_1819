from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect
from .models import Pelis
from django.urls import reverse
from django.contrib.auth.decorators import login_required

import re
from .serializers import PelisSerializer

import logging
logger = logging.getLogger(__name__)

# Create your views here.


# ------------------------------------------------------------------------------
# BUSCADORES
# ------------------------------------------------------------------------------

def buscador(request):

	'''
	Página que muestra el formulario para introducir el actor
	'''

	logger.debug("Accediendo al buscador de películas")

	return render(request,"mainBuscador.html")


# ------------------------------------------------------------------------------
# TAREA 4
# ------------------------------------------------------------------------------

def mongoengine_year(request, entrada):

	'''
	Mostrar las primeras películas a partir de la entrada de un actor
	(haciendo uso de mongoengine)
	'''
	regex = re.compile(entrada)
	pelis = Pelis.objects(actors = regex)

	context = {
		'lista': pelis,
		'entrada': True,
	}

	return render(request, "salida.html", context)


# ------------------------------------------------------------------------------
# TAREA 5
# ------------------------------------------------------------------------------

def pelis_que_sale(request, entrada):

	'''
	Mostrar las primeras películas a partir de la entrada de un actor
	(haciendo uso de mongoengine)
	'''
	regex = re.compile(entrada)
	pelis = Pelis.objects(actors = regex)

	context = {
		'lista': pelis,
		'entrada': True,
		'resultados': pelis.count(),
	}

	logger.debug('Películas protagonizadas por el actor %s' % entrada)

	return render(request, "salida1.html", context)

# ------------------------------------------------------------------------------

def formulario(request):

	'''
	Página que muestra el formulario para introducir el actor
	'''

	logger.debug("Accediendo al formulario para el actor")

	return render(request,"formulario1.html")

# ------------------------------------------------------------------------------

def peliculas_actor(request):

	'''
	Obtenemos las películas en donde dicho actor es protagonista
	'''

	actor = request.POST.get('actor')

	logger.debug('Películas protagonizadas por el actor')

	return HttpResponseRedirect(reverse('pelis_que_sale',args=[actor]))


# ------------------------------------------------------------------------------
# TAREA 6
# ------------------------------------------------------------------------------

@login_required
def informacion_pelicula(request, id):

	'''
	Se muestra información relevante de la película a partir de su ID
	'''
	# Buscamos la película solo por el ID
	pelicula = Pelis.objects(id=id)

	context = {
		'pelicula': pelicula[0],
		'id': True,
	}

	logger.debug('Mostrada información de la película con id %s' % id)

	return render(request,"informacion_pelis.html",context)

# ------------------------------------------------------------------------------

def formulario_id(request):

	'''
	Página que muestra el formulario para introducir el id
	'''

	logger.debug("Accediendo al formulario para el identificador")

	return render(request,"id.html")

# ------------------------------------------------------------------------------

def peliculas_id(request):

	'''
	Obtenemos la películas de dicho ID
	'''

	id = request.POST.get('id')

	logger.debug('Mostrada información de la película')

	return HttpResponseRedirect(reverse('informacion_pelicula',args=[id]))


# ------------------------------------------------------------------------------
# TAREA 7
# ------------------------------------------------------------------------------

@login_required
def crud(request):

	'''
	Obtemos la página de inicio del CRUD y visualizamos las 100 primeras
	películas ordenadas por actor
	'''

	peliculas = Pelis.objects().all().order_by('actor')[:100]
	context = {
		'lista' : peliculas,
		'general': True,
	}

	logger.debug("Accediendo al CRUD")

	return render(request, "crud.html", context)

# ------------------------------------------------------------------------------

@login_required
def crear_pelicula(request):

	'''
	Función que permite crearnos una película, a partir de los campos:
	titulo, año, director, actores, genero, puntuacion, duracion
	'''

	# Para crear una película se debe de hacer uso del método POST
	if(request.method == "POST"):
		parametros = request.POST
		actores = parametros['actores'].split(", ")
		genero = parametros['genero'].split(", ")

		# Creamos la película
		pelicula = Pelis(title = parametros['titulo'],
						 year = parametros['año'],
						 director = parametros['director'],
						 actors = actores,
						 genres = genero,
						 imdb = {'rating' : parametros['puntuacion']},
						 runtime = parametros['duracion'])

		# Guardamos la pelicula
		pelicula.save()

	logger.debug("Película creada correctamente")

	return HttpResponseRedirect(reverse('crud'))

# ------------------------------------------------------------------------------

@login_required
def borrar_pelicula(request,id):

	'''
	Función que permite borrar una película, a partir de su identificador
	'''

	pelicula = Pelis.objects(id=id)

	if(pelicula.count()==1):
		pelicula.delete()

	logger.debug("Película borrada correctamente")

	return HttpResponseRedirect(reverse('crud'))

# ------------------------------------------------------------------------------

def editar_pelicula(request,id):

	'''
	Función que permite editar una película a partir de su identificador, y
	los campos: titulo, año, director, actores, genero, puntuacion, duracion
	'''
	pelicula = Pelis.objects(id=id)

	# Se da la opción de que el usuario cambie solo datos concretos
	if(request.method == "POST"):
		parametros = request.POST

		if(parametros.get('titulo')!= ''):
			pelicula.update_one(title=parametros.get('titulo'))

		if (parametros.get('año') != ''):
			pelicula.update_one(year=parametros.get('año'))

		if (parametros.get('director') != ''):
			pelicula.update_one(director=parametros.get('director'))

		if (parametros.get('actores') != ''):
			actores = parametros.get('actores').split(", ")
			pelicula.update_one(actors=actores)

		if (parametros.get('genero') != ''):
			genero = parametros.get('genero').split(", ")
			pelicula.update_one(actors=genero)

		if (parametros.get('puntuacion') != ''):
			pelicula.update_one(imdb__rating=parametros.get('puntuacion'))

		if (parametros.get('duracion') != ''):
			pelicula.update_one(runtime=parametros.get('duracion'))

	logger.debug("Película editada correctamente")

	return HttpResponseRedirect(reverse('crud'))


# ------------------------------------------------------------------------------
# TAREA 12
# ------------------------------------------------------------------------------

def api_pelis(request):

	'''
	Función para la API que lista todas las películas (GET) y
	permite añadir (POST)
	'''

	# Método para listar
	if request.method == 'GET':
		pelis = Pelis.objects.all()[:10]
		serializer = PelisSerializer(pelis, many=True)

		return JsonResponse(serializer.data, safe=False)

	# Método para añadir
	if request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = PelisSerializer(data=data)

		if serializer.is_valid():
			serializer.save()

			return JsonResponse(serializer.data, status=201)

	logger.debug('Error')

	return JsonResponse(serializers.errors, status=400)

# ------------------------------------------------------------------------------

def api_peli(request, id):

	'''
	Función para la API que permite listar todas las películas (GET),
	modificarlas (PUT) y/o borrarlas (DELETE)
	'''

	try:
		peli = Pelis.objects().get(id=id)
	except:
		return HttpResponse(status=404)  # No encontrado

	# Método para listar
	if request.method == 'GET':
		serializer = PelisSerializer(peli)
		return JsonResponse(serializer.data)

	# Método para modificar
	if request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = PelisSerializer(data=data)

		peli.title 		 = data.title
		peli.title       = data.title
		peli.year        = data.year
		peli.rated       = data.rated
		peli.runtime     = data.runtime
		peli.countries   = data.countries
		peli.genres      = data.genres
		peli.director    = data.director
		peli.writers     = data.writers
		peli.actors      = data.actors
		peli.plot        = data.plot
		peli.poster      = data.poster
		peli.imdb        = data.imdb
		peli.tomato      = data.tomato
		peli.metacritic  = data.metacritic
		peli.awards      = data.awards
		peli.type        = data.type

		peli.save()
		return JsonResponse(serializer.data, status=200)

	# Método para borrar
	if request.method == 'DELETE':
		peli.delete()
		return HttpResponse(status=200)  # No encontrado
