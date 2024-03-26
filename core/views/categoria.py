from rest_framework.viewsets import ModelViewSet

from core.models import Acessorios, Categoria
from core.serializers import AcessoriosSerializer, CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer