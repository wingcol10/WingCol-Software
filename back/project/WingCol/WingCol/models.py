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
		max_length=100
	)
	roles = models.PositiveSmallIntegerField(choices=ROLES)
	activo = models.BooleanField(default=True)
	# password_reset_token = models.CharField(max_length=255, null=True, blank=True)
	objects = UsersManager()

	USERNAME_FIELD = 'user_id'
	REQUIRED_FIELDS = ['email', 'roles']

	def set_password(self, raw_password):
		self.password = make_password(raw_password)

	def check_password(self, raw_password):
		return check_password(raw_password, self.password)


class AdministraDor(models.Model):
	class Genero(models.TextChoices):
		MASCULINO = 'M', 'Masculino'
		FEMENINO = 'F', 'Femenino'
		OTRO = 'O', 'Otro'

	user_id = models.OneToOneField(NormalUser, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=50)
	segundo_nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	segundo_apellido = models.CharField(max_length=50)
	genero = models.CharField(max_length=1, choices=Genero.choices)
	telefono = models.PositiveIntegerField()

class Cliente(models.Model):
	class Genero(models.TextChoices):
		MASCULINO = 'M', 'Masculino'
		FEMENINO = 'F', 'Femenino'
		OTRO = 'O', 'Otro'

	class TipoDocumento(models.TextChoices):
		CC = 'CC', 'Cédula de Ciudadanía'
		TI = 'TI', 'Tarjeta de Identidad'
		CE = 'CE', 'Cédula de Extranjería'
		PA = 'PA', 'Pasaporte'

	user_id = models.OneToOneField(NormalUser, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=50)
	segundo_nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	segundo_apellido = models.CharField(max_length=50)
	tipo_documento = models.CharField(max_length=2, choices=TipoDocumento.choices)
	fecha_nacimiento = models.DateField()
	genero = models.CharField(max_length=1, choices=Genero.choices)	
	telefono = models.PositiveIntegerField()
	direccion = models.CharField(max_length=50)
	direccion_facturacion = models.CharField(max_length=50)
	

class Root(models.Model):
	user_id = models.OneToOneField(NormalUser, on_delete=models.CASCADE)

class Tarjetas(models.Model):
	class TipoTarjeta(models.TextChoices):
		DEBITO = 'D', 'Débito'
		CREDITO = 'C', 'Crédito'
	id_tarjeta = models.PositiveIntegerField(primary_key=True) 
	id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	tipo_tarjeta = models.CharField(max_length=20, choices=TipoTarjeta.choices)
	vvc = models.PositiveIntegerField()
	fecha_expiracion = models.DateField()
	saldo = models.IntegerField()

class Vuelos(models.Model):
	class EstadoVuelo(models.TextChoices):
		PROGRAMADO = 'P', 'Programado'
		REALIZADO = 'R', 'Realizado'
		CANCELADO = 'C', 'Cancelado'

	class TipoVuelo(models.TextChoices):
		NACIONAL = 'N', 'Nacional'
		INTERNACIONAL = 'I', 'Internacional'

	id_vuelo = models.PositiveIntegerField(primary_key=True)
	ciudad_origen = models.CharField(max_length=25)
	ciudad_destino = models.CharField(max_length=25)
	precio = models.PositiveIntegerField()
	fecha_salida = models.DateTimeField()
	fecha_llegada = models.DateTimeField()
	tipo = models.CharField(max_length=20, choices=TipoVuelo.choices)
	estado = models.CharField(max_length=20, choices=EstadoVuelo.choices)
	

class Sillas(models.Model):
	class ClaseAsiento(models.TextChoices):
		ECONOMICA = 'E', 'Clase económica'
		PRIMERA_CLASE = 'P', 'Primera clase'

	class EstadoAsiento(models.TextChoices):
		LIBRE = 'L', 'Libre'
		RESERVADO = 'R', 'Reservado'
		OCUPADO = 'O', 'Ocupado'

	id_silla = models.PositiveIntegerField(primary_key=True)
	id_vuelo = models.ForeignKey(Vuelos, on_delete=models.CASCADE)
	ubicacion = models.CharField(max_length=5)
	clase = models.CharField(max_length=20, choices=ClaseAsiento.choices)
	estado = models.CharField(max_length=20, choices=EstadoAsiento.choices)

class ComprasReservas(models.Model):
	class Estado(models.TextChoices):
		COMPRADO = 'COM', 'Comprado'
		RESERVADO = 'RES', 'Reservado'
		CANCELADO = 'CAN', 'Cancelado'
	id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	id_vuelo = models.ForeignKey(Vuelos, on_delete=models.CASCADE)
	id_cr = models.PositiveIntegerField(primary_key=True)
	estado = models.CharField(max_length=20, choices=Estado.choices)
	valor = models.PositiveIntegerField()

class Tiquete(models.Model):
	class ClaseVuelo(models.TextChoices):
		ECONOMICA = 'E', 'Clase económica'
		PRIMERA_CLASE = 'P', 'Primera clase'
	class TipoEquipaje(models.TextChoices):
		PERSONAL = 'EP', 'Equipaje personal'
		MANO = 'EM', 'Equipaje de mano'
		MALETA = 'MB', 'Maleta de bodega'

	id_tiquete = models.PositiveIntegerField(primary_key=True)
	id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	id_vuelo = models.ForeignKey(Vuelos, on_delete=models.CASCADE)
	clase = models.CharField(max_length=20, choices=ClaseVuelo.choices)
	tipo_equipaje = models.CharField(max_length=20, choices=TipoEquipaje.choices)
	verificacion = models.CharField( max_length=50)

class Busquedas(models.Model):
	id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	ciudad_origen = models.CharField(max_length=25)
	ciudad_destino = models.CharField(max_length=25)
	fecha = models.DateTimeField(auto_now_add=True)
