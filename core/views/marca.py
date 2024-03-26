from rest_framework.viewsets import ModelViewSet

from core.models import Acessorios, Categoria, Cor, Marca
from core.serializers import AcessoriosSerializer, CategoriaSerializer, CorSerializer, MarcaSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer