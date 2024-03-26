from rest_framework.serializers import ModelSerializer

from core.models import Acessorios, Categoria

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"