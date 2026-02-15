from django.contrib.auth.models import User
import os

username = 'alumnodb'
password = 'alumnodb'
email = 'admin@example.com'

if not User.objects.filter(username=username).exists():
  print('Creando superusuario...')
  User.objects.create_superuser(username, email, password)
else:
  print('El superusuario ya existe, saltando paso.')
