# mi_app/viewsets.py
from rest_framework_mongoengine import viewsets
from .models import Pelis
from .serializers import PelisSerializer

class PelisViewSet(viewsets.ModelViewSet):
		queryset = Pelis.objects.all()[:10]
		lookup_field = 'id'
		serializer_class = PelisSerializer
