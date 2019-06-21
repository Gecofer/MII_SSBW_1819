from django.db import models
from mongoengine import *
from mongoengine.queryset.visitor import Q

connect('movies', host='mongo')

# Create your models here.

class Pelis(Document):
	title     = StringField(required=True)
	year      = IntField(min_value=1900,max_value=2222)
	rated     = StringField()
	runtime   = IntField()
	countries = ListField(StringField())
	genres    = ListField(StringField())
	director  = StringField()
	writers	  = ListField(StringField())
	actors	  = ListField(StringField())
	plot	  = StringField()
	poster	  = StringField()
	imdb	  = DictField()
	tomato	  = DictField()
	metacritic= IntField()
	awards 	  = DictField()
	type 	  = StringField()

	# {'type', 'plot', 'director', 'writers', 'imdb', 'genres', 'awards',
	# 'actors', 'metacritic', 'tomato', 'poster'}"
