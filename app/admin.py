from django.contrib import admin
from .models import Articulo, Producto

# Register your models here.
admin.site.register(Producto)
admin.site.register(Articulo)