from django.contrib import admin
#Importarmos el modelo post
from .models import Post
# Register your models here.
#Registro de modelo para hacerlo visible en la pagina de administracion
# Link de administracion
#http://127.0.0.1:8000/admin/. 
admin.site.register(Post)
