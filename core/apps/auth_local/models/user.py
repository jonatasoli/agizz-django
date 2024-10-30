import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .user_manager import UserManager
from core.apps.base.models.custom_models import ModelMixin


class User(AbstractBaseUser, PermissionsMixin, ModelMixin):
    TYPE_CHOICES = (
        ('client', 'Client'),
        ('producer', 'Producer'),
        ('super admin', 'Super Admin'),
    )

    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    cpf_cnpj = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['cpf_cnpj']

    class Meta:
        app_label = 'auth_local'
        ordering = ['-created_at']
