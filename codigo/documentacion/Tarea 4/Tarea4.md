# Tarea 4

La primer aparte es hacer una consulta con pymongo, luego para la aplicación definitiva.

1. Creamos el fichero: `docker-compose.yml`

2. Nos descargamos el contenedor: `docker-compose build`

3. Hacemos `docker-compose up` (en un terminal)

4. Importamos el fichero JSON a la raíz:
`docker-compose exec mongo mongoimport --db movies --collection pelis --file /datos/movieDetails.json`

5. Accedemos a `http://localhost:8081`

Tenemos que tener 3 contenedores:

Para acceder al contenedor: `docker-compose exec mongo /bin/bash`

----

Poner en el requirements.txt

mongoengine==0.16

----

## Usando mongoengine
En nuestra aplicación definitiva usaremos monogoengine, que es un ORM muy inspirado en el model de Django.

Haremos una nueva aplicación en nuestro proyecto:

`docker-compose run web python manage.py startapp pelis`

Nos crea una carpeta pelis y nos vamos a `models.py` y copiamos

~~~
from mongoengine import *

connect('movies', host='mongo')

class Pelis(Document):
	title     = StringField(required=True)
	year      = IntField(min_value=1900)
	rated     = StringField()
	runtime   = IntField()
	countries = ListField(StringField())
~~~
