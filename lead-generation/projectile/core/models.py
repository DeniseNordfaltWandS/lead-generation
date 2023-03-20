from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from core.managers import UserManager
from common.abstracts import TimestampModel

class UserLanguage(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)

class Language(models.Model):
    name = models.CharField(max_length=50)

class User(AbstractBaseUser, PermissionsMixin, TimestampModel):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=20)
    born_at = models.IntegerField()
    address = models.CharField(max_length=200)
    languages = models.ManyToManyField('Language', through='UserLanguage')
    linkedin_url = models.URLField(max_length=1024, null=True, blank=True)
    github_url = models.URLField(max_length=1024, null=True, blank=True)
    portfolio_url = models.URLField(max_length=1024, null=True, blank=True)
    accepted_terms_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



