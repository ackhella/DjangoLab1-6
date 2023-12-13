from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.forms import DateTimeField
from .managers import UserAccountManager
from django.utils import timezone

# Create your models here.


class Article(models.Model):

    name = models.CharField('article name', max_length=100, null=True)

    author = models.CharField('author', max_length=200, null=True)

    date_created = models.DateTimeField('date created', null=True)

    description = models.TextField('main text', null=True)

    cover = models.ImageField(upload_to="gallery", null=True, blank=True)


class Account(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Meta:
    verbose_name = 'Account'
    verbose_name_plural = 'Accounts'
