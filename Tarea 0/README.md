## Tarea 0: Entorno de desarrollo con docker-compose

> **Pincha [aquí](https://github.com/Gecofer/MII_SSBW_1819/blob/master/Tarea%200/Tarea0.md) para ver cómo se hizo la Tarea 0**

Usaremos [docker-compose](https://docs.docker.com/compose/) como entorno de desarrollo durante toda la asignatura.

Empezamos [instalando docker-compose](https://docs.docker.com/compose/install/). También está en el apt-get de ubuntu, pero [puede no estar en la última versión](https://linuxize.com/post/how-to-install-and-use-docker-compose-on-ubuntu-18-04/).

Seguiremos los pasos de [Quickstart: Compose and Django](https://docs.docker.com/compose/django/), En principio no usamos un servicio aparte para la BD, de manera que el archivo **docker-compose.yml** queda:

~~~
version: '3'

services:
	web:
		build: .
		command: python3 manage.py runserver 0.0.0.0:8000
		volumes:
			- .:/code
		ports:
			- "8000:8000"
~~~

Creamos entonces un proyecto:

~~~
$ docker-compose run web django-admin.py startproject mi_sitio_web .
~~~

y cambiamos los permisos

~~~
$ sudo chown -R $USER:$USER .
~~~

puesto que docker crea los archivos como root.

Podemos comprobar que funciona iniciando el contenedor

~~~
$ docker-compose up
~~~

que pondrá el servidor de desarrollo en http://localhost:8000

Podemos ahora usar el python del contenedor:

~~~
$ docker-compose run web python
~~~

o

~~~
$ docker-compose run web python hola_mundo.py
~~~
