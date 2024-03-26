from rest_framework.serializers import ModelSerializer

from core.models import Acessorios, Categoria, Cor

class CorSerializer(ModelSerializer):
    class Meta:
        model = Cor
        fields = "__all__"