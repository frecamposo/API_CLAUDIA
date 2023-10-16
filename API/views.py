from django.shortcuts import render
    # dispone de paginas pre-diseñadas para presentar datos
from rest_framework import generics
    # indica el model y campos a serializar
from .serializers import UsuarioSerializer,RecetaSerializer,CategoriaSerializer
    # cuales seran los datos disponibles en la pagina
from .models import Usuario,Receta,Categoria


# Create your views here.

class UsuarioViewSet(generics.ListCreateAPIView):
    # cuales son los datos a mostrar
    queryset = Usuario.objects.all()
    # como seran serializados
    serializer_class = UsuarioSerializer
# Create your views here.


class RecetaViewSet(generics.ListCreateAPIView):
    # cuales son los datos a mostrar
    queryset = Receta.objects.all()
    # como seran serializados
    serializer_class = RecetaSerializer


class CategoriaViewSet(generics.ListCreateAPIView):
    # cuales son los datos a mostrar
    queryset = Categoria.objects.all()
    # como seran serializados
    serializer_class = CategoriaSerializer


class RecetaEliminarViewSet(generics.DestroyAPIView):
    serializer_class = RecetaSerializer
    def get_queryset(self):
        id_persona = self.kwargs['id']
        return Receta.objects.filter(idreceta=id_persona)
    def delete(self,request,id=None):
        id_persona = id
        print('--'+id_persona)
        p = Receta.objects.filter(idreceta=id_persona)
        if p:
            p.delete()
            return Response({'message':'producto eliminado'},status = status.HTTP_200_OK)
        return Response({'error':'no existen reg con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
