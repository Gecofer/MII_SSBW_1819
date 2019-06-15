## Tarea 11: AJAX, ES6 fetch

> **Pincha [aquí](https://github.com/Gecofer/MII_SSBW_1819/blob/master/Tarea%2010/Tarea11.md) para ver cómo se hizo la Tarea 11**


En esta tarea vamos a añadir un nuevo campo númerico a cada peli, que aumente o disminulla 'me gusta' o 'no me gusta'.

Pondremos iconos de _me gusta_, y _no me gusta_, podemos usar [Font Awesone](https://fontawesome.bootstrapcheatsheets.com), o los que sugiere [Boostrap](https://getbootstrap.com/docs/4.0/extend/icons/).

Los botones haran una llamada al servidor, que responderá con el valor correspodiente para insertarlo en la página.

Para la comunicación asíncrona con el servidor, podemos usar [AJAX de jQuery](https://uniwebsidad.com/libros/fundamentos-jquery/capitulo-7/metodos-ajax-de-jquery?from=librosweb), o bien [fetch de ES6](https://developer.mozilla.org/es/docs/Web/API/Fetch_API/Utilizando_Fetch). Si usamos una petición POST o PUT al servidor, que sería lo lógico puesto que vamos a modificar la Base de Datos, tenemos que incluir el token [csrf de Django](https://stackoverflow.com/questions/8614947/jquery-and-django-csrf-token). Ver [Using the Fetch Api with Django Rest Framework](https://gist.github.com/marteinn/3785ff3c1a3745ae955c).

El valor que se envie del servidor lo podemos volver a poner en su sitio con el método [html](http://api.jquery.com/html/) de jQuery.
