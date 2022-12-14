"""User model."""
import uuid as uuid

from django.contrib.auth import models as django_models
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(django_models.BaseUserManager):

    def get_by_natural_key(self, username):
        return self.get(**{'{}__iexact'.format(
            self.model.USERNAME_FIELD): username})

    def create_user(self, email, username=None, password=None,
                    **other_fields):
        if not email:
            raise ValueError(_('Please provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, password=password,
                          username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username=None,
                         password=None, **other_fields):
        """
        Create and return a `User` with superuser admin rights.
        Superuser admin rights means that this use is an admin that can do
        anything they want.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')
        user = self.create_user(email, username, password, **other_fields)
        user.save()
        return user


class User(django_models.AbstractBaseUser,
           TimeStampedModel,
           PermissionsMixin):
    """
    User model for the user creation
    """
    uuid = models.UUIDField(unique=True, max_length=500,
                            default=uuid.uuid4,
                            editable=False,
                            db_index=True, blank=False, null=False)
    email = models.EmailField(_('Email'), db_index=True, unique=True)
    is_staff = models.BooleanField(_('Is staff'), default=True)
    is_active = models.BooleanField(_('Is Active'), default=True)
    username = models.CharField(_('Username'), max_length=255,
                                blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-created']

    def get_full_name(self):
        return self.username

    def __str__(self):
        """
        Returns a string representation of this `User`.
        This string is used when a `User` is printed in the terminal
         - which is an email for now.
        """
        return f'{self.email}'

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
