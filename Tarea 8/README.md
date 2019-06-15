## Tarea 8: Autentificación, Autorización, y Registro de eventos

> **Pincha [aquí](https://github.com/Gecofer/MII_SSBW_1819/blob/master/Tarea%208/Tarea8.md) para ver cómo se hizo la Tarea 8**

En esta tarea completaremos el ['back-end'](https://en.wikipedia.org/wiki/Front_and_back_ends) de nuestra aplicación añadiendo la autentificación de usarios y un sistema de registro de eventos (logs).

Django tiene todo lo necesario para el autentificar usuarios, modelo en la BD, formularios, etc. Pero hay un plugin para Django que facilita todo esto: [django-allauth](https://www.intenct.nl/projects/django-allauth/), que incluye también plantillas, el registro en uno o dos pasos (con activación de la cuenta por e-mail), gestión de la contraseña olividada con tokens, y delegacion de la autentificación en redes sociales usando [oauth2](https://solidgeargroup.com/oauth2-protocolo-de-autorizacion?lang=es).

En [Django-allauth tutorial](https://wsvincent.com/django-allauth-tutorial/), hay una guia para instalarlo.

Hay que tener algún usuario creado, y regenerar la BD cuando se instale.

Podemos personalizar los templates, usando los que tiene en [templates](https://github.com/pennersr/django-allauth/tree/master/allauth/templates/account) y poniendolos en una carpeta `templates/accounts`. Si hay problemas consulta [overriding default templates of django-allauth](https://stackoverflow.com/questions/9437545/overriding-default-templates-of-django-allauth).

Ahora ya podremos usar el [user object de django](https://docs.djangoproject.com/en/2.2/topics/auth/default/) desde el `request`, y gestinar la autorización de usuarios en las vistas, simplemente incluyendo el decorador `@login_required` antes de cada 'vista' de Django: [login required decorator](https://docs.djangoproject.com/en/2.2/topics/auth/default/#the-login-required-decorator).

### HTTPS

Cuando usamos contraseñas, debemos usar un protocolo cifrado para evitar su [robo](https://en.wikipedia.org/wiki/Session_hijacking). Para esto debemos conectar nuestra aplicación a un servidor web como [nginx](https://nginx.org/en/), que se encargará de la gestión de [https](https://nginx.org/en/docs/http/configuring_https_servers.html).

Pondremos entonces un servicio más en nuestro **docker-compose.yml**:

~~~
version: '3'
  services:
    nginx:
      image: nginx:alpine
      ports:
        - "80:80"
        - "443:443"
      volumes:
        - ./conf:/etc/nginx/conf.d:ro
        - ./cert:/etc/ssl/private:ro
      depends_on:
        - web
    ...
    web:
      build: .
      command: python3 manage.py runserver 0.0.0.0:8000
      volumes:
        - .:/code
~~~        

En el directorio **cert**, pondremos un par de archivos con una [pareja de claves generadas](https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-nginx-in-ubuntu-18-04) a este próposito, y en el directorio **conf** el archivo de configuración de nginx:

~~~
server {
  listen 80 default_server;
  server_name _;

  # redirecciona todo a https
  return 301 https://$host$request_uri;
}

server {
  listen 443 ssl;
  server_name _;

  # la pareja de claves
  ssl_certificate /etc/ssl/private/nginx.crt;
  ssl_certificate_key /etc/ssl/private/nginx.key;
  keepalive_timeout   70;

  ssl_protocols       TLSv1 TLSv1.1 TLSv1.2;
  ssl_ciphers         AES128-SHA:AES256-SHA:RC4-SHA:DES-CBC3-SHA:RC4-MD5;
  ssl_session_cache   shared:SSL:10m;
  ssl_session_timeout 10m;

  location  ~ ^/(miapp|admin|accuonts) {
		try_files $uri @proxy_to_app;
  }

  # proxy inverso
  location @proxy_to_app {
	proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
	proxy_set_header Host $http_host;
	proxy_redirect off;
	proxy_pass   http://web:8000;
  }
}
~~~

### Registro de eventos

Django tiene un módulo para registro: [Django Logging](https://docs.djangoproject.com/en/2.2/topics/logging/) basado en el de [python](https://docs.python.org/3.6/library/logging.html).

La configuración del registro, se pone el archivo `settings.py`, y puede ser algo así:

~~~python
LOG_FILE = 'mi_archivo_de.log'

LOGGING = {
	 'version': 1,
	 'disable_existing_loggers': False,

	  'formatters': {
	       'verbose': {
             'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
              'datefmt' : "%d/%b/%Y %H:%M:%S"
	        },
           'simple': {
             'format': '%(levelname)s [%(name)s:%(lineno)s] %(message)s'
	           },
	       },

	       'handlers': {
	           'file': {
	               'level': 'INFO',
	               'class': 'logging.FileHandler',
	               'filename': os.path.join(BASE_DIR, LOG_FILE),
	               'formatter': 'verbose',
	               'mode':'w'
	            },
	            'console': {
	                'level': 'DEBUG',
	                'class': 'logging.StreamHandler',
	                'formatter': 'simple'
	            }
	        },

	        'loggers': {
	            'django': {
	                'handlers':['file'],
	                'propagate': True,
	                'level':'ERROR',
	             },
	             'mi_instagram': {
	                'handlers': ['file', 'console'],
	                 'level': 'DEBUG',
	              },
	          }
	     }
~~~

y ya podemos [usar el logging](https://lincolnloop.com/blog/django-logging-right-way/)
