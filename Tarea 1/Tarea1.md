## Tarea 1: Ejercicios de Python

### Apuntes de Clase

**¿Qué es un servidor web?** Un servidor web es un programa que utiliza el protocolo de transferencia de hipertexto, HTTP (Hypertext Transfer Protocol), para servir los archivos que forman páginas web a los usuarios, en respuesta a sus solicitudes, que son reenviados por los clientes HTTP de sus computadoras. Debemos tener en cuenta: _navegador - servidor web - aplicación_. Visualizo todo desde el navegador.

**Protocolos**: HTTP, HTTPS (HTTP con secure), FTP (File Transfer Protocol), IPP (para la impresoras), mailto (para el mail), DNS (Domain Name System). Si se pone solo `localhost`, por defecto es HTTP (`http://localhost...`), ya que se omite la primera parte. Además, por defecto, está en el puerto 80 `http://localhost:80`, que necesita privilegios de superusuario, pero nosotros vamos a usar el 8000.

- http://localhost:8000/ejercicio1: el servidor es como una llamada a un procedimiento remoto.

**Django** ya tiene un servidor web, que no es como el usual, el de Django está pensado para desarrollo, para ver cuando falla el código...

En esta tarea vamos hacer una mini aplicación. Además, para cada ejercicio vamos a tener una ruta distinta, es decir,`localhost/ejercicioX`. Cada vez que hagamos este requiremento será así.

- http://localhost:8000/ejercicio1
- http://localhost:8000/ejercicio2
- http://localhost:8000/ejercicio3
- ...

**¿Cómo sería una respuesta en HTML? ¿Cómo es en HTML "Hola Mundo"?**: Usando etiquetas:

~~~html
<html>
  Hola mundo
</html>
~~~

Podemos poner el _body_, en Python esto es muy sencillo:

~~~python
print(<html> Hola mundo <!html>)
~~~

Deberíamos de poner 3 comillas, para tener saltos de línea:

~~~python
salida = '''
          <html>
            Hola mundo
          <!html>
         '''

print(salida)
~~~

-----

### Ejercicio

**Vamos a crear una aplicación startapp a partir de lo que creamos en la [Tarea 0](https://github.com/Gecofer/MII_SSBW_1819/tree/master/Tarea%200), en donde hicimos un proyecto. Pues ahora vamos a crear una aplicación.**

Prepararemos nuestro entorno de desarrollo para que la entrada y salida de los ejercicios de python sean a través del navegador. Para esto crearemos una aplicación dentro del proyecto de la tarea anterior, ejecutando la siguiente línea al mismo nivel que donde está el fichero `docker-compose`:

~~~
$ docker-compose run web python manage.py startapp ejercicios
~~~

- _web_: servicio
- _contenedor_: SO
- _manage.py_: para dar órdenes a Django
- _volumes_: donde está montado

Y se nos creará una carpeta llamada `ejercicios`:

- **composeexample**: es el proyecto
- **ejercicios**: es la aplicacion

Apuntamos esa carpeta creada en el archivo `proyecto/settings.py`. El `settings.py` va a la configuración inicial y el fichero `urls.py` va para el enrutador, donde se pone cada url que función va a ejecutar. El _framework_ está pensado para que cada parte del programa estén en archivos distintos, ya que el codigo está en un solo archivo.

Ahora tocamos en el proyecto (`composeexample`):

~~~python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',  # para mandar un tipo de archivo en la cabecera
    'django.contrib.sessions',      # para tener las sesiones
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
~~~

Ahí están las aplicaciones que ya trae el _framework_, entonces tenemos que poner la aplicación que hemos creada "ejercicios":

~~~python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes', # para mandar un tipo de archivo en la cabecera
    'django.contrib.sessions', # para tener las sessiones
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ejercicios',
]
~~~

Prepararemos el _dispatcher_ de nuestro _framework_ para que la entrada y la salida a los ejercicios sea con el navegador. Tendremos que cambiar el enrutador principal `proyecto/urls.py`:

~~~python
# proyecto/urls.py

django.conf.urls import include, url
django.contrib import admin
urlpatterns=[
    url(r'^ejercicicios/',include('ejercicios.urls')),
    # url('ejercicicios/',include('ejercicios.urls')),
    url(r'^admin/',admin.site.urls),
]
~~~

- ^: expresión regular
- r: raw, para que no interprete el "/n"

Cuando la url empieza por ejercicio, se va a un archivo que se llama `urls.py`, en donde tenemos que importar las librerías

~~~python
from django.conf.urls import include, url # importamos las librerías
django.conf.urls.url                      # otra manera de importarlas
~~~

Ya hemos terminado la aplicación, ahora tenemos que crear un archivo que se llama `urls.py` dentro de la carpeta `ejercicios`. El encaminamiento de los urls lo ponemos el archivo `ejercicios/urls.py`. Ahí voy a poner las urls y que función van hacer cada una, y será cuando se ponga lo de `localhost/ejercicio1`.

~~~python
path('hola_mundo', views.hola_mundo), # entrada str
# que muestre hola mundo en la raiz /hola_mundo
~~~

El programa principal del código va a estar en `views.py` y ahí es donde vamos hacer los ejercicios de python.

~~~python
from django.shortcuts import HttpResponse

def hola_mundo(request, usuario):
    salida = '''
        <html>
            ...
            Hola %s
            ...
        </html>''' % (usuario)

    return HttpResponse(salida)
~~~

Y ponemos el hola mundo en `views.py`:

~~~python
from django.shortcuts import render
from django.shortcuts import HttpResponse

def hola_mundo(request):
    # request un objeto donde está la informacion que le llega
    # del nevegador (lo que te llega)

    # salida es un string
    salida = '''<html>
                    ...
                    Hola mundo
                    ...
                </html>
              '''
    # devolvemos la variable para HTTP
    return (HttpResponse(salida))
~~~

Y ejecutamos el programa con `docker-compose up`.

![](imagenes/1.png)
