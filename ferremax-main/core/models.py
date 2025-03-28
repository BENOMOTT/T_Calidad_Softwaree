from django.db import models
import geocoder

# Create your models here.
class Marca(models.Model):
    marca = models.CharField(max_length=70)
    
    def __str__(self):
        return self.marca


class Producto(models.Model):
    nombre = models.CharField(max_length=60)
    precio = models.IntegerField()
    medidas = models.CharField(max_length=60)
    imagen = models.ImageField(upload_to="productos",null=True)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT )

    def __str__(self):
        return self.nombre
    
class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=50)
	zipcode =  models.CharField(max_length=20)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")
    
class Tutorial (models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.TextField()
    imagen  = models.ImageField(upload_to="tutoriales",null=True)

    def __str__(self):
        return self.nombre
    

    
class Ciudad (models.Model):
    nom_ciudad = models.CharField(max_length=60)

    def __str__(self):
        return self.nom_ciudad
    
class Comuna (models.Model):
    nom_comuna = models.CharField(max_length=60)
    nom_ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT )

    def __str__(self):
        return self.nom_comuna
    
class Usuario_direccion (models.Model):
    Nombre = models.CharField(max_length=60)
    Rut = models.CharField(max_length=60)
    calle = models.CharField(max_length=100)
    Numero = models.CharField(max_length=60)       
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT )
    comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT )

    def __str__(self):
        return self.Nombre
    

    
access_token = 'pk.eyJ1IjoiZW50cm9waXR0IiwiYSI6ImNsamo3Y2NobzA1dmwzbW90bnFkaG9teWsifQ.FyYRKsSJSe7xF1fKFlQW7w'

class Address(models.Model):
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address,key=access_token)
        g = g.latlng  # [lat,long]
        self.lat = g[0]
        self.long = g[1]
        return super(Address, self).save(*args, **kwargs)
    



