## Tarea 12: API REST

> **Pincha [aquí](https://github.com/Gecofer/MII_SSBW_1819/blob/master/Tarea%2012/Tarea12.md) para ver cómo se hizo la Tarea 12**

En esta tarea añadiremos una API REST a nuestra aplicación, siguiendo el [tutorial](https://www.django-rest-framework.org/tutorial/1-serialization/#introduction) que viene con la docuemenación de [Django Rest Framework](https://www.django-rest-framework.org) y la adaptación a mongoengine: [Django + MongoDB = Django REST Framework Mongoengine](https://medium.com/@vasjaforutube/django-mongodb-django-rest-framework-mongoengine-ee4eb5857b9a). También How to setup [Django + Django REST Framework + Mongo?](https://leadwithoutatitle.wordpress.com/2018/03/21/how-to-setup-django-django-rest-framework-mongo/)

Añadimos a **requirements.txt**:

~~~python
...
djangorestframework
django-rest-framework-mongoengine
~~~

y en el **settings.py**:

~~~python
INSTALLED_APPS = [
...
'rest_framework',
'rest_framework_mongoengine'
]
~~~

Haremos dos versiones del `API`, una donde respondamos desde funciones en **views.py**, y otra aprovechando el enrutador, y las 'class views' que incluye el framework.


### API desde funciones

Seguimos los pasos de la [primera parte del tutorial](https://www.django-rest-framework.org/tutorial/1-serialization/#introduction) y creamos lo serializadores, unas clases similares a las de formularios, que se van a encargar de codificar/decodificar los datos a/desde el request al model: creamos un archivo **serializers.py**

~~~python
# mi_app/serializers.py
# adaptado para mongoengine
from rest_framework_mongoengine import serializers
from .models import Pelis

class PelisSerializer(serializers.DocumentSerializer):
	class Meta:
		model = Pelis
		fields = '__all__'
~~~

Aquí podriamos incluir validadores, logs, etc, sobrescribiendo los métodos de la clase para crear, borrar, modificar, listar.

Podremos comprobar que funciona:

~~~
> python manage.py shell
> from pelis.serializers import PelisSerializer
> from pelis.models import Pelis
> serializer = PelisSerializer(Pelis.objects.all(), many=True)
> print (serializer)
> print (serializer.data)
> from rest_framework.renderers import JSONRenderer
> content = JSONRenderer().render(serializer.data)
> print(content)
~~~

Ahora ya podremos preparar el url dispatcher y las vistas para nuestro api, en **urls.py**

~~~python
# mi_app/urls.py
...
path('api_pelis',    views.api_pelis),  # GET lista todas, POST añade
path('api_peli/<id>', views.api_peli),  # GET lista una,   PUT modifica, DELETE borrra
~~~

Y en **views.py**

~~~python
# mi_app/views.py
...
from django.http import JsonResponse

# Listar todas, Añadir
def api_pelis(request):
	if request.method == 'GET':
		pelis = Pelis.objetcts.all()[:10]
		serializer = PelisSerializer(fotos, many=True)
		return JsonResponse(serializer.data, safe=False)

	if request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = PelisSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)

	logger.debug('Error')
	return JsonResponse(serializers.errors, stauts=400)

# Listar, Modificar, Borrar
def api_peli(request, id):
	try:
		peli = Pelis.objects().get(id=id)
	except:
		logger.debug('Peli no encontrada '+id)
		return HttpResponse(status=404)  # No encontrado

	if request.method == 'GET':
		serializer = PelisSerializer(peli)
		return JsonResponse(serializer.data)

	if request.method == 'PUT':
		...

	if request.method == 'DELETE':
			...
~~~

### APIS desde clases viewsets

Seguimos ahora [Django + MongoDB = Django REST Framework Mongoengine](https://medium.com/@vasjaforutube/django-mongodb-django-rest-framework-mongoengine-ee4eb5857b9a) para incluir respuesta desde las clases que incluye DRF. En un nuevo archivo **viewsets.py**:

~~~python
# mi_app/viewsets.py
from rest_framework_mongoengine import viewsets
from .model import Pelis
from .serializers import PelisSerializer

class PelisViewSet(viewsets.ModelViewSet):
		queryset = Pelis.objetcs.all()[:10]
		lookup_field = 'id'
		serializer_class = PelisSerializer
...
# Aquí también podriamos sobreescribir los métodos, de leer, añadir, borrar, etc
~~~

Y modificamos el enrutador para incluir además las rutas predefinidas de DRF y el interface de depuración en **urls.py**:

~~~python
# mi_app/urls.py
from django.conf.urls import include, url
from rest_framework import routers
from .viewsets import PelisViewSet
...

router = routers.DefaultRouter()
router.register('pelis', PelisViewSet, 'peli')

urlpatterns = [
	url('api', include(router.urls)), # Incluye todo el API CRUD
   ...
]
~~~

Y el api sale en: https://localhost/pelis/apipeli/

### Autentificación (optativo)

[How to Use JWT Authentication with Django REST Framework](https://simpleisbetterthancomplex.com/tutorial/2018/12/19/how-to-use-jwt-authentication-with-django-rest-framework.html)
