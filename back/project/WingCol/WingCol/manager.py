from django.contrib.auth.models import BaseUserManager

class UsersManager(BaseUserManager):
	def create_user(self, user_id, email, password = None):
		if not email:
			raise ValueError("Los Usuarios Deben Tener Correo")
		if not user_id:
			raise ValueError("Los Usuarios Deben Tener Un Documento de Identidad")
		
		user = self.model(
			user_id = user_id,
			email = self.normalize_email(email),
		)
		user.set_password(password)
		user.save(using = self.db)
		return user

	# def create_client(self, user_id, email, password, *args):
	# 	pass

	# def create_administrator(self, user_id, email, password, *args):
	# 	pass
	
	def create_superuser(self, user_id, email, password = None):
		user = self.create_user(
			user_id = user_id,
			email = email, 
			password = password
		)
		user.isadmin = True
		user.save(using = self.db)
		return user