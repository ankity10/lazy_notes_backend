from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager


# class User(AbstractBaseUser, PermissionsMixin):
# 	username = models.CharField(max_length=32, primary_key=True)
# 	email = models.CharField(max_length=32, unique=True)
# 	password = models.CharField(max_length=32)
# 	full_name = models.CharField(max_length=32)

# 	objects = UserManager()

# 	USERNAME_FIELD ='username'
# 	REQUIRED_FIELDS = []



	#user_id = models.IntegerField()

class Clients(models.Model,):
	client_id = models.CharField(max_length=50)
	username = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):              
		return self.client_id

# Create your models here.
