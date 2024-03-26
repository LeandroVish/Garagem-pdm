from rest_framework.viewsets import ModelViewSet

from core.models import Acessorios, Categoria, Cor
from core.serializers import AcessoriosSerializer, CategoriaSerializer, CorSerializer

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer