from django.db import models
from .manager import UsersManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.hashers import make_password, check_password

class NormalUser(AbstractBaseUser, PermissionsMixin):
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
	roles = models.PositiveSmallIntegerField(choices=ROLES)
	# password_reset_token = models.CharField(max_length=255, null=True, blank=True)
	
	objects = UsersManager()

	USERNAME_FIELD = 'user_id'
	REQUIRED_FIELDS = ['email', 'roles']

	def set_password(self, raw_password):
		self.password = make_password(raw_password)

	def check_password(self, raw_password):
		return check_password(raw_password, self.password)


class Administrator(models.Model):
	class Sex(models.TextChoices):
		MASCULINO = 'M', 'Masculino'
		FEMENINO = 'F', 'Femenino'
		OTRO = 'O', 'Otro'

	user = models.OneToOneField(NormalUser, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	second_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	second_last_name = models.CharField(max_length=50)
	sex = models.CharField(max_length=1, choices=Sex.choices)
	phone = models.PositiveIntegerField()

class Client(models.Model):
	class Sex(models.TextChoices):
		MASCULINO = 'M', 'Masculino'
		FEMENINO = 'F', 'Femenino'
		OTRO = 'O', 'Otro'

	class TypeDocument(models.TextChoices):
		CC = 'CC', 'Cédula de Ciudadanía'
		TI = 'TI', 'Tarjeta de Identidad'
		CE = 'CE', 'Cédula de Extranjería'
		PA = 'PA', 'Pasaporte'

	user = models.OneToOneField(NormalUser, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	second_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	second_last_name = models.CharField(max_length=50)
	type_document = models.CharField(max_length=2, choices=TypeDocument.choices)
	date_birth = models.DateField()
	sex = models.CharField(max_length=1, choices=Sex.choices)	
	phone = models.PositiveIntegerField()
	address = models.CharField(max_length=50)
	facturation_address = models.CharField(max_length=50)
	

class Root(models.Model):
	user = models.OneToOneField(NormalUser, on_delete=models.CASCADE)

class Tarjetas(models.Model):
	id_tarjeta = models.PositiveIntegerField(primary_key=True) 
	id_cliente = models.ForeignKey(Client, on_delete=models.CASCADE)
	TipoTarjeta = models.TextChoices("Débito", "Crédito")
	tipo_tarjeta = models.CharField(max_length=30, choices=TipoTarjeta)
	vvc = models.PositiveIntegerField()
	fecha_expiracion = models.DateField()
	saldo = models.IntegerField()

class Vuelos(models.Model):
	pass

class Sillas(models.Model):
	id_silla = models.PositiveIntegerField(primary_key=True)
	id_vuelo = models.ForeignKey(Vuelos, on_delete=models.CASCADE)
	ubicacion = models.CharField(max_length=5)
	Clase = models.TextChoices()
	clase = models.CharField()

class ComprasReservas(models.Model):
	pass


