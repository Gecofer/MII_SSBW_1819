## Tarea 4: Base de Datos MongoDB

> **Pincha [aquí](https://github.com/Gecofer/MII_SSBW_1819/blob/master/Tarea%204/Tarea4.md) para ver cómo se hizo la Tarea 4**

En esta tarea instalaremos y usaremos la base de datos no-sql [MongoDB](https://docs.mongodb.com/manual/tutorial/getting-started/).

Crearemos un servicio para mongodb en nuestro **docker-compose.yml**, usando la [image oficial de mongodb](https://hub.docker.com/_/mongo).

~~~
version: '3'
  services:
    mongo:
      image: mongo:4.0
      volumes:
        - ./datos_db:/data/db
        - .:/datos

    mongo-express:
      image: mongo-express
      ports:
        - 8081:8081
      depends_on:
        - mongo

    web:
      build: .
      command: python manage.py runserver 0.0.0.0:8000
      volumes:
        - .:/code
      ports:
        - 8000:8000
      links:
        - mongo
      depends_on:
        - mongo
~~~

donde se ha añadido un servicio más: [mongo-express](https://github.com/mongo-express/mongo-express#readme), para tener una GUI de la base de datos. El segundo volumen del servicio mongo, servirá para importar los datos iniciales de la BD.

Los datos los bajamos de https://raw.githubusercontent.com/steveren/docs-assets/charts-tutorial/movieDetails.json y los importamos a la bd con la utilidad `mongoimport`

~~~
$ docker-compose exec mongo mongoimport --db movies --collection pelis --file /datos/movieDetails.json
~~~

y podremos ver que todo haya ido bien en http://localhost:8081. Editando un documento desde la GUI podremos ver la estructura de la colección.

### Usando pymongo

Haremos algunas consultas en la BD usando el cliente [pymongo](http://api.mongodb.com/python/current/tutorial.html). Para instalarlo hay que poner en el archivo **requeriments.txt**

~~~python
...
mongoengine==0.16
~~~

Así se instalarán los dos clientes de MongoDB que vamos a usar, puesto que monogoengine es una capa de software por encima de pymongo.

Hacer algunas consultas que usen pymongo.

### Usando mongoengine

En nuestra aplicación definitiva usaremos [monogoengine](http://mongoengine.org), que es un [ORM](https://programarfacil.com/blog/que-es-un-orm/) muy inspirado en el [model](https://docs.djangoproject.com/en/2.2/topics/db/models/) de Django.

Haremos una nueva aplicación en nuestro proyecto:

~~~
$ docker-compose run web python manage.py startapp pelis
~~~

y en el archivo **models.py**:

~~~python
# models.py
-----------

from mongoengine import *

connect('movies', host='mongo')

class Pelis(Document):
	title     = StringField(required=True)
	year      = IntField(min_value=1900)
	rated     = StringField()
	runtime   = IntField()
	countries = ListField(StringField())
	...
~~~

Hacer las mismas consultas que con pymongo.
