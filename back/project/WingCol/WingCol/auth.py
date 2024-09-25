from rest_framework import authentication, permissions, exceptions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authtoken.models import Token
from .models import NormalUser, Administrador, Root, Cliente

class ClientAuthentication(authentication.BaseAuthentication):
	def authenticate(self, request):
		token = request.headers.get('Authorization')
		if not token:
			return None
		try:
			token = token.split(' ')[1]
			user_id = Token.objects.get(key=token).user_id
			user = NormalUser.objects.get(user_id=user_id)
			if user.roles == 1:
				return (user, None)
			else:
				raise exceptions.AuthenticationFailed('No Permissions Provided')
		except NormalUser.DoesNotExist:
			return None
		except:
			raise exceptions.AuthenticationFailed('Invalid token')