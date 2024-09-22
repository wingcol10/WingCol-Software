from django.db import models
from .manager import UsersManager
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin


class NormalUser(AbstractBaseUser):
	ROLES = (
		(1, "Cliente"),
		(2, "Administrador"),
		(3, "Root")
	) 
	user_id = models.PositiveBigIntegerField(unique=True)
	email = models.EmailField(
		verbose_name="direccion de correo electrónico",
		max_length=255,
		unique=True
	)
	# password = models.CharField()
	roles = models.PositiveSmallIntegerField(choices=ROLES)
	
	objects = UsersManager()

	USERNAME_FIELD = 'user_id'
	REQUIRED_FIELDS = ['email', 'roles']


class Administrator(models.Model):
	user_id = models.OneToOneField(NormalUser, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	second_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	second_last_name = models.CharField(max_length=50)
	genero = models.TextChoices('Masculino', 'Femenino', 'Otro')
	telefono = models.PositiveIntegerField()

class Client(models.Model):
	user_id = models.OneToOneField(NormalUser, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	second_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	second_last_name = models.CharField(max_length=50)
	tipo_documento = models.TextChoices(
									'Cédula de Ciudadanía', 
									'Tarjeta de Identidad', 
									'Cédula de Extranjería', 
									'Pasaporte')
	date_birth = models.DateField()
	

class Root(models.Model):
	user_id = models.OneToOneField(NormalUser, on_delete=models.CASCADE)

class Tarjetas(models.Model):
	id_tarjeta = models.PositiveIntegerField(primary_key=True) 
	id_cliente = models.ForeignKey(Client, on_delete=models.CASCADE)
	TipoTarjeta = models.TextChoices("Débito", "Crédito")
	tipo_tarjeta = models.CharField(max_length=30, choices=TipoTarjeta)
	vvc = models.PositivoIntegerField()
	fecha_expiracion = models.DateField()
	saldo = models.IntegerField()

class Vuelos(models.Model):
	pass

class Sillas(models.Model):
	id_silla = models.PositiveIntegerField(primary_key=True)
	id_vuelo = models.ForeignKey(Vuelos, on_delete=models.CASCADE)
	ubicacion = models.CharField(max_length=5)
	Clase = models.TextChois
	clase = models.CharField()

class ComprasReservas(models.Model):
	pass


