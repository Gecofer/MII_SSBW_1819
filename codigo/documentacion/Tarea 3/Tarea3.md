Un programa que analiza un archivo de texto, lo ideal es 1990. Sacar los de “1990”.

import re
match = re.search(r'([\w.-]+)@([\w.-]+)', str)


read // para leer línea a linea

Busca, pones paréntesis.
Buscas el patrón de “Popularity in 1990” los 4 digits de 1990, poner para que coja fechas
group


import re
m = re.search('(?P<dia>\d\d)-(?P<mes>\d\d)-(?P<año>\d\d)', texto)
                          # Si no tienen nombre sería
dia = m.group('dia')      # m.group(1)
mes = m.group('mes')      # m.group(2)
año = m.group('año')      # m.group(3)


En group.dia tiene el resultado de la abstracción


Leer los archivos, buscar patrones y que te devuelva los nombres.
Dada un archivo que están por año, devolver una lista

siempre vamos a trabajar con Python y HTML de forma separada, en donde en la carpeta template va a estar todo lo de HTML

Dos formas de hacer el ejercicio


1. Devolver los nombres más populares en un año (lista)
2. Django template —> Template Django buscar en google
    1. Creamos un directorio “template” con archivos HTML dentro de la carpeta ejercicios
    2. El archivo HTML que será el que saque
    3. Dentro nos creamos un archivo qu se llama “nombres.html”: ahi sacamos la pagina HTML. Esa es la manera de tener el HTML separado del código python. No mezclar código HTML con código Python.
    4. <html>
    5.
    6.   <head>
    7.       <title>Ejercicio de expresiones regulares</title>
    8.   </head>   
    9.
    10.   <body>
    11.     Estadísticas del año —> va en lengujae de plantilla que se llama (mostacho)
    12.   </body>   
    13. Estadísticas del año {{ año }} este año es una variable, puedes mandar una lista
3. Es
<html>

  <head>
      <title>Ejercicio de expresiones regulares</title>
  </head>

  <body>
    Estadísticas del año {{ año }}

    <table>
      <tr>
        <th> Nombre </th>
        <th> Número </th>
      </tr>

      {% for l in lista %}
        <tr>
          <td> {{ l.nombre }} </td>
          <td> {{ l.numero }} </td>
        </tr>
      {% endfor %}

    </table>

  </body>

</html>


Ahora me voy al views e importo pongo una  librería

from django.shortcuts import render


render(request, 'templates/nombres.html', <la variable que mandas>)

def ejercicio_expresiones_regulares(request, entrada):

    context = {
        'año': 1990,
        'lista': lista de objetos
          en lista cada elemento es un diccionario
          {'nombre': 'pepe', 'numero': 2},
                {'nombre': 'juan', 'numero': 28},
                // esta lista la hemos sacado de la BD
    }

    return render(request, 'templates/nombres.html', context)


Esta manera    se llama "jinja" (ya lo veremos más adelante)


tambien podemos hacer que devuelva "requets HTTP"


RSS : ver que es

http://ep00.epimg.net/rss/tags/ultimas_noticias.xml

view-source:http://ep00.epimg.net/rss/tags/ultimas_noticias.xml

Para coger este archivo, lo importamos con el requirements

r = requests.get('htpps://')

Importar "requests" en el requiriements

requests==2.21.0


Lo de los bebes ya no lo hacemos:

ponemos [url][imagen]


Sacamos todos los enlaces de una pagina web y ponemos


Vamos buscando estas cosas:

<image>
<url>
https://ep00.epimg.net/iconos/v1.x/v1.0/logos/cabecera_portada.png
</url>
<title>Logotipo de EL PAÍS</title>
<link>https://elpais.com/</link>
</image>

Y mostramos en la html final, por ejemplo las fotos, o los títulos

una ruta con titulares y otra con fotos



docker-compose build para instalar el del requiremets

hacer con la funcion de requests, por lo que hay que importar el archivo


obtener los titulares
<title><\[!CDATA\](.+?)\]\]<\/title>

<title><!\[CDATA\[(.+?)\]\]<\/title>

coger lo de view-source:web.xml


la semana que vienne vemos los ejercicios de la asignatura, para crear, leer, eliminar registros
