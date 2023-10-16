#from django.conf.urls import url
from django.urls import re_path as url
from rest_framework import urlpatterns
from API import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^api/usuarios/$',views.UsuarioViewSet.as_view()),
    url(r'^api/recetas/$',views.RecetaViewSet.as_view()),
    url(r'^api/categorias/$',views.CategoriaViewSet.as_view()),
    url(r'^api/recetas_eliminar/(?P<id>.+)/$',views.RecetaEliminarViewSet.as_view()),
]

urlpatterns=format_suffix_patterns(urlpatterns)