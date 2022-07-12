from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin , BaseUserManager
# Create your models here.
class CustomAccountManager(BaseUserManager):
    def create_user(self,email,username,password,**other_fields):
        email = self.normalize_email(email)
        user = self.model(email = email,username = username,**other_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,username,password,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)
        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        return self.create_user(email,username,password,**other_fields)


class NewUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique = True)
    username = models.CharField(max_length = 150, unique = True)
    ign = models.CharField(max_length = 150)
    password = models.CharField(max_length = 150)
    phone = models.BigIntegerField(default=0000000000)
    startdate = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_organizer = models.BooleanField(default = False)
    teams = ArrayField(ArrayField(models.CharField(max_length = 150)),null=True)
    dp = models.ImageField(default = "../static/images/logo")
    

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


    