from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.template import Context, Template
from django.urls import reverse

import re # Librería para Expresiones Regulares
import random
import requests
import logging

from pymongo import *

# from .forms import PostForm

# from .models import Pelis

client = MongoClient('mongo', 27017)
db = client.movies
pelis = db.pelis


# ------------------------------------------------------------------------------
# TAREA 1
# ------------------------------------------------------------------------------

'''
def hola_mundo(request):
    # 'request' es un objeto donde está la informacion que le llega
    # del nevegador (lo que te llega)

    # La variable salida es un 'string'
    salida = <html>
                ...
                Hola mundo
                ...
             </html>

    return (HttpResponse(salida)) # Devolvemos la variable para HTTP
'''

# ------------------------------------------------------------------------------

def hola_mundo(request, usuario):

    '''
    Función que muestra por pantalla "hola" y el usuario introducido en la ruta
    '''

    # Introducimos al suario por la ruta
    salida = '''<html>
                    Hola %s
                </html>
              ''' % (usuario)

    return (HttpResponse(salida)) # Devolvemos la variable para HTTP


# ------------------------------------------------------------------------------
# TAREA 2
# ------------------------------------------------------------------------------

def tarea2_ejercicio1(request, lista):

    '''
    Given a list of strings, return the count of the number of
    strings where the string length is 2 or more and the first
    and last chars of the string are the same.

    Note: python does not have a ++ operator, but += works.
    '''

    # http://localhost:8000/ejercicios/tarea2/ejercicio1/a-aaa-aa-aaaa-a
    # Tiene 2 elementos de longitud mayor a 2

    # En algún momento, puede que se necesite romper una cadena grande en una
    # más pequeña. Para ello, se utiliza la función "split". Lo que hace
    # es dividir o romper una cadena y añadir los datos a una matriz de
    # cadenas usando un comando separador definido. Si no se define ningún
    # separador cuando se llama a la función, se utilizarán los espacios en
    # blanco por defecto. En términos más sencillos, el
    # separador es un carácter definido que se colocará entre cada variable
    entrada = lista.split("-") # ponemos como separado un guión

    cont = 0

    # Comprobamos que el primer y el último caracter son iguales
    if entrada[0] == entrada[-1]:
        # Iteramos sobre la lista y obtenemos el recuento del número de string
        # donde la longitud de la cadena es de 2 o más
        for elem in entrada:
            if len(elem)>2:
                cont = cont + 1

        salida = '''
                    <html>
                        Tiene %d elementos de longitud mayor a 2
                    </html>
                 ''' % (cont)

    # El primer y el último caracter no son iguales --> no hacemos nada
    else:
        salida = '''
                    <html>
                        El primer y el último caracter no son iguales
                    </html>
                 '''

    return (HttpResponse(salida)) # Devolvemos la variable para HTTP

# ------------------------------------------------------------------------------

def tarea2_ejercicio2(request, lista):

    '''
    Given a list of numbers, return a list where
    all adjacent == elements have been reduced to a single element,
    so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
    modify the passed in list.
    '''

    # http://localhost:8000/ejercicios/tarea2/ejercicio2/a-aaa-aa-aaaa-a-a-a-aaa
    # La lista original era ['a', 'aaa', 'aa', 'aaaa', 'a', 'a', 'a', 'aaa'] y
    # sin repetidos queda ['a', 'aa', 'aaa', 'aaaa']

    # Guardamos la lista de entrada
    entrada_con_repetidos = lista.split("-")

    # Usamos la función "split" para añadir los datos a una matriz de
    # cadenas usando un comando separador definido (guiones)
    entrada = set(lista.split("-"))

    # Ordenamos esa lista
    entrada = sorted(entrada)

    salida = '''<html>
                    La lista original era %s y sin repetidos queda % s
                </html>
              ''' % (entrada_con_repetidos, entrada)

    return (HttpResponse(salida)) # Devolvemos la variable para HTTP

# ------------------------------------------------------------------------------

def tarea2_ejercicio3(request, entrada):

    '''
    Given a string s, return a string made of the first 2
    and the last 2 chars of the original string,
    so 'spring' yields 'spng'. However, if the string length
    is less than 2, return instead the empty string.
    '''

    # http://localhost:8000/ejercicios/tarea2/ejercicio3/s
    # {}

    # http://localhost:8000/ejercicios/tarea2/ejercicio3/sol
    # sol

    # http://localhost:8000/ejercicios/tarea2/ejercicio3/sola
    # sola

    # http://localhost:8000/ejercicios/tarea2/ejercicio3/spring
    # spng

    # http://localhost:8000/ejercicios/tarea2/ejercicio3/clase
    # clse

    # Si la cadena es menor a 2, devolvemos vacío
    if len(entrada) < 2:
        entrada = {}
    # Si la cadena es 3 ó 4, devolvemos la palabras
    elif (len(entrada) == 3 or len(entrada)) == 4:
        entrada = entrada
    # Si la cadena es mayor a 4
    elif len(entrada) > 4:
        entrada = entrada[0] + entrada[1] + entrada[-2] + entrada[-1]

    salida = '%s' % (entrada)

    return (HttpResponse(salida)) # Devolvemos la variable para HTTP

# ------------------------------------------------------------------------------

def tarea2_ejercicio4(request, entrada):

    '''
    Given a string, if its length is at least 3,
    add 'ing' to its end.
    Unless it already ends in 'ing', in which case
    add 'ly' instead.
    If the string length is less than 3, leave it unchanged.
    '''

    # http://localhost:8000/ejercicios/tarea2/ejercicio4/spring
    # springly

    # http://localhost:8000/ejercicios/tarea2/ejercicio4/sprin
    # sprining

    # Dada una cadena, si su longitud es de al menos 3
    if (len(entrada) >= 3):
        # Si no termina en "ing" añadir "ing" al final
        if (entrada[-3:] != "ing" ):
            entrada = entrada + "ing"
        # Si termina en "ing", añadir "ly" al final
        elif (entrada[-3:] == "ing" ):
            entrada = entrada + "ly"

    # Si la longitud de la cadena es inferior a 3, no cambie la palabra
    else:
        entrada = entrada

    salida = '%s' % (entrada)

    return (HttpResponse(salida)) # Devolvemos la variable para HTTP

# ------------------------------------------------------------------------------

def diccionario_mimico(filename):

    # Devolvemos el diccionario "mímico" mapeando cada palabra a la lista
    # de palabras que la siguen. Construimos un diccionario "mímico" que mapea
    # cada palabra que aparece en el archivo a una lista de todas las palabras
    # que siguen inmediatamente a esa palabra en el archivo.
    diccionario_mimico = {}
    prev = ''

    # Leemos un fichero
    with open("file.txt") as f:
        mensaje = f.read()

    # Eliminamos las mayúsculas y los signos de puntuación
    mensaje = mensaje.lower();
    mensaje = re.sub(r'[^\w\s]','', mensaje)

    # Hacer un "split()" en un espacio en blanco para obtener todas las
    # palabras del archivo
    mensaje = mensaje.split()

    # Creamos el diccionario mimico
    # Iteramos las palabras del texto de entrada
    # palabra ['prev']
    # Añadimos la siguiente palabra a la lista
    for palabra in mensaje:
        if not prev in diccionario_mimico:
          diccionario_mimico[prev] = [palabra]
        else:
          diccionario_mimico[prev].append(palabra)

        prev = palabra

    # Devolvemos el diccionario mimico creado
    return diccionario_mimico


def visualizar_diccionario_mimico(diccionario_mimico, palabra):

  lista_diccionario = []

  # Dado el diccionario mimico mímico y la palabra inicial,
  # vamos a visualizar 200 palabras al azar
  for i in range(200):
    lista_diccionario.append(palabra + "")
    # Usaremos la cadena vacía como primera palabra
    palabra_siguiente = diccionario_mimico.get(palabra)

    # Poner None si no se encuentra
    if not palabra_siguiente:
        palabra_siguiente = diccionario_mimico['']

    # El módulo estándar de python 'random' incluye un
    # random.choice(list) método que selecciona un elemento aleatorio
    # de una lista no vacía
    palabra = random.choice(palabra_siguiente)

  # http://elclubdelautodidacta.es/wp/2013/10/python-troceando-y-recomponiendo-strings/
  # Vamos hacer el proceso inverso de la función "split()", es decir, dada una
  # lista de strings, fusionarla en una única cadena empleando determinado
  # carácter como separador
  texto = (' '.join(lista_diccionario))

  return texto;


def tarea2_ejercicio5(request):

    '''
    Read any text file specified on the command line.
    Do a simple split() on whitespace to obtain all the words in the file.
    Rather than read the file line by line, it's easier to read
    it into one giant string and split it once.

    Build a "mimic" dict that maps each word that appears in the file
    to a list of all the words that immediately follow that word in the file.
    The list of words can be be in any order and should include
    duplicates. So for example the key "and" might have the list
    ["then", "best", "then", "after", ...] listing
    all the words which came after "and" in the text.
    We'll say that the empty string is what comes before
    the first word in the file.

    With the mimic dict, it's fairly easy to emit random
    text that mimics the original. Print a word, then look
    up what words might come next and pick one at random as
    the next work.

    Use the empty string as the first word to prime things.
    If we ever get stuck with a word that is not in the dict,
    go back to the empty string to keep things moving.
    Note: the standard python module 'random' includes a
    random.choice(list) method which picks a random element
    from a non-empty list.

    For fun, feed your program to itself as input.
    Could work on getting it to put in linebreaks around 70
    columns, so the output looks better.
    '''

    # http://localhost:8000/ejercicios/tarea2/ejercicio5

    # Mostramos el contenido del fichero
    f = open ('file.txt','r')
    fichero = f.read()
    f.close()

    # Devolvemos el diccionario creado
    diccionario = diccionario_mimico("file.txt")

    # Creamos el nuevo texto
    # Dado el diccionario mimico y la palabra inicial,
    # imprime 200 palabras al azar.
    texto = visualizar_diccionario_mimico(diccionario, '')

    # Visualizamos todo a la salida
    salida = '''
                <html> <h2>Texto original </h2> %s
                       <h2>Diccionario mimico </h2> %s
                       <h2>Texto resultante </h2> %s
                </html>
             ''' % (fichero, diccionario, texto)

    return HttpResponse(salida)


# ------------------------------------------------------------------------------
# TAREA 3
# ------------------------------------------------------------------------------

def ejercicio_expresiones_regulares(request):

    context = {
        'año': 1990,
        'lista': [
            {'nombre': 'pepe', 'numero': 2},
            {'nombre': 'juan', 'numero': 28},
        ]
    }

    return render(request, 'nombres.html', context)


# ------------------------------------------------------------------------------

def extraer_titulares_imagenes(request):

    '''
    Función que nos permite extraer los titulares e imágenes de un periódio,
    a partir del contenido XML
    '''

    contenido = ""
    titulos = []
    imagenes = []
    context = {}

    # La URL de la que vamos a extraer el contenido
    url = 'http://ep00.epimg.net/rss/elpais/portada.xml'

    # Comprobamos que la URL escogida devuele estatus 200
    web = requests.get(url)
    if(web.status_code == 200): contenido = web.text

    # La estructura de los títulos en la URL de XML
    extraer_titulares = re.findall(r'<title><\!\[CDATA\[(.+?)\]\]><\/title>',
                              contenido)

    # La estructura de los títulos en la URL de XML
    extraer_imagenes = re.findall(r'<enclosure url="(.+?)"', contenido)

    # Recorremos todos los de la página
    for titular in extraer_titulares:
        titulos.append({'titular': titular})

    for imagen in extraer_imagenes:

        imagenes.append({'imagen': imagen})

    # Los guardamos, para mostrarlos en la página HTML
    context = {
        'titulos': titulos,
        'imagenes': imagenes
    }

    return render(request, 'periodico.html', context)


# ------------------------------------------------------------------------------
# TAREA 4
# ------------------------------------------------------------------------------

def pymongo(request):

    '''
    Mostrar las 10 primeras películas (haciendo uso de pymongo)
    '''

    lista = []
    lista = pelis.find(limit=10)
    print(pelis.count_documents({}))
    print(lista)
    context =  {'lista': lista}

    return render(request, "salida.html", context)

# ------------------------------------------------------------------------------

def pymongo_year(request, entrada):

    '''
    Mostrar las primeras películas a partir de la entrada de un año
    (haciendo uso de pymongo)
    '''

    lista = []
    lista = pelis.find({ "year": int(entrada) })
    #print(pelis.count_documents({}))
    #print(lista)
    #for x in pelis.find({ "year": entrada }):
    #    lista.append(x)

    context =  {'lista': lista}

    return render(request, "salida.html", context)

# ------------------------------------------------------------------------------

def pymongo_actor(request, entrada):

    '''
    Mostrar las primeras películas a partir de la entrada de un actor
    (haciendo uso de mongoengine)
    '''

    lista = []
    lista = pelis.find({"actors": {"$regex": entrada}})

    context = {
        'lista': lista,
        'actor': True
    }

    return render(request, "salida.html", context)
