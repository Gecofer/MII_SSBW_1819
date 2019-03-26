## Tarea 2: Ejercicios de Python

- [Ejercicio 1](#ej1)
- [Ejercicio 2](#ej2)
- [Ejercicio 3](#ej3)
- [Ejercicio 4](#ej4)
- [Ejercicio 5](#ej5)

### Ejercicio 1 <a name="ej1"></a>

Dada una lista de string, devuelve la cuenta del número de string donde la longitud del string es 2 o más y la primera y la última letra del string son la misma.

Nota: python no tiene un operador ++, pero += funciona.

~~~python
# urls.py

# entrada str, lista separada por espacios, guiones o comas
path('tarea2/ejercicio1/<lista>', views.tarea2_ejercicio1),
~~~

~~~python
# views.py

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

    # Comprobamos que el primer y el último carácter son iguales
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
~~~

Hemos cogido la siguiente lista _a-aaa-aa-aaaa-a_, y se puede apreciar que existen solo dos ítems de la lista con dos elementos mayor a dos: _aaa_ y _aaaa_

- http://localhost:8000/ejercicios/tarea2/ejercicio1/a-aaa-aa-aaaa-a

  ![](imagenes/1_0.png)

Por otro lado, para poder obtener el número de elementos que tiene la lista mayor a dos, dicha lista debe tener el primer y el último carácter igual: _a-aaa-aa_

- http://localhost:8000/ejercicios/tarea2/ejercicio1/a-aaa-aa

    ![](imagenes/1_1.png)


### Ejercicio 2 <a name="ej2"></a>

Dada una lista de números, devuelve una lista donde todos los elementos adyacentes == se han reducido a un solo elemento, así que[1, 2, 2, 3] devuelve[1, 2, 3]. Puede crear una nueva lista o modificar la lista pasada.

~~~python
# urls.py

# entrada str, lista separada por espacios, guiones o comas
path('tarea2/ejercicio2/<lista>', views.tarea2_ejercicio2),
~~~

~~~python
# views.py

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
~~~

Por ejemplo, la lista original es ['a', 'aaa', 'aa', 'aaaa', 'a', 'a', 'a', 'aaa'] y sin repetidos queda ['a', 'aa', 'aaa', 'aaaa'].

- http://localhost:8000/ejercicios/tarea2/ejercicio2/a-aaa-aa-aaaa-a-a-a-aaa

  ![](imagenes/2_0.png)


### Ejercicio 3 <a name="ej3"></a>

### Ejercicio 4 <a name="ej4"></a>

### Ejercicio 5 <a name="ej5"></a>
