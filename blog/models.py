#From e import es usada para llamar otras funciones o archivos
#y poder incluir o llamar algunas partes de codigo
from django.db import models
from django.utils import timezone

#class:Define la creacion de un objeto, palabra clave o reservada CLASE
#Post: nombre de la clase debe evitarse caracteres especiales y 
#espacios en blanco, siempre empiezan con mayuscula
#modelo.Model: identifica a una clase modelo de Django que debe ser
#guardada en la base de datos
class Post(models.Model):
	#DEFINICION DE PROPIEDADES DE LA CLASE
	#Propiedad que define la clave primaria de relacion con otras
	#clases
	author = models.ForeignKey('auth.User')
	#Tipo de dato string con numero limitado de caracteres
	title = models.CharField(max_length=200)
	#Textos largos sin limite-contenido del post
	text = models.TextField()
	#Fecha y hora
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)
	#Funcion o metodo propio de la clase, nombre a gusto
	#Metodo que no devuelve valores
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	#Doble guion bajo dunder
	#Metodo que devuelve un resultado [return]
	def __str__(self):
		return self.title