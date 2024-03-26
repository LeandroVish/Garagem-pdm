from rest_framework.serializers import ModelSerializer

from core.models import Acessorios, Categoria, Cor, Marca

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"