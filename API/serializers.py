from django.db.models import fields
from rest_framework import serializers
from .models import Usuario,Receta,Categoria

# definir una clase con la tabla a serializar y los
# campos
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"

class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = "__all__"


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"