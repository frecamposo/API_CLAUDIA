from django.contrib import admin
from .models import Categoria,DetallePedido,Pedido,Receta,Repartidor,Usuario
# Register your models here.
admin.site.register(Categoria)
admin.site.register(DetallePedido)
admin.site.register(Pedido)
admin.site.register(Receta)
admin.site.register(Repartidor)
admin.site.register(Usuario)