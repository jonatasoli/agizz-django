from typing import Type
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(
            self, email: str, cpf_cnpj: str, password: str = None
    ) -> Type[BaseUserManager]:
        user = self.model(email=email)
        user.cpf_cnpj = cpf_cnpj
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
            self, email: str, cpf_cnpj: str, password: str
    ) -> Type[BaseUserManager]:
        user = self.create_user(email=email, cpf_cnpj=cpf_cnpj, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
