## Tarea 5: CSS Frameworks y formularios

> **Pincha [aquí](https://github.com/Gecofer/MII_SSBW_1819/blob/master/Tarea%205/Tarea5.md) para ver cómo se hizo la Tarea 5**

En esta tarea incorporaremos alguno de los [frameworks CSS 'responsive'](https://www.skysilk.com/blog/2018/6-best-css-frameworks-2019/) a la tarea anterior.

Haremos una consulta del estilo http://localhost:8000/ejercicios/pelis que sale/Clark Gable"

Luego haremos una nueva app en nuestro proyecto:

~~~
$ docker-compose run web python manage.py startapp pelis
~~~

incorporaremos el model con `mongoengine`, y haremos una consulta similar usando un [formulario](https://developer.mozilla.org/es/docs/Learn/HTML/Forms/Your_first_HTML_form).
