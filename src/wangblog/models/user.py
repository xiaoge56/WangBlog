# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
file: user.py
time   : 16/4/15 下午8:44  
"""
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.db import models
import warnings
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class UserManager(UserManager):
    pass
    # def create_user(self, username, email, password=None):
    #     """
    #     Creates and saves a User with the given email, date of
    #     birth and password.
    #     """
    #     if not email:
    #         raise ValueError('Users must have an email address')
    #
    #     user = self.model(
    #         username=username,
    #         email=self.normalize_email(email),
    #     )
    #
    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user
    #
    # def create_superuser(self, username, email, password):
    #     """
    #     Creates and saves a superuser with the given email, date of
    #     birth and password.
    #     """
    #     user = self.create_user(email,
    #         password=password,
    #         username=username
    #     )
    #     user.is_admin = True
    #     user.save(using=self._db)
    #     return user


class User(AbstractBaseUser):
    username = models.CharField(_('username'), max_length=128, unique=True)
    # this column is called first_name for legacy reasons, but it is the entire
    # display name
    userkey = models.CharField(_('user key'), max_length=128, null=True, unique=True)
    name = models.CharField(_('name'), max_length=200, blank=True,
                            db_column='first_name')
    email = models.EmailField(_('email address'), blank=True)
    organization_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.IntegerField(unique=True, default=123456, null=True)
    sub_domain = models.CharField(max_length=255, unique=True, null=True)
    is_admin = models.BooleanField(default=True)
    is_staff = models.BooleanField(
        _('staff status'), default=True,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(
        _('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    is_superuser = models.BooleanField(
        _('superuser status'), default=False,
        help_text=_('Designates that this user has all permissions without '
                    'explicitly assigning them.'))
    is_managed = models.BooleanField(
        _('managed'), default=False,
        help_text=_('Designates whether this user should be treated as '
                    'managed. Select this to disallow the user from '
                    'modifying their account (username, password, etc).'))

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    # class Meta:
    #     app_label = 'wangblog'
    #     db_table = 'auth_user'
    #     verbose_name = _('user')
    #     verbose_name_plural = _('users')

    def delete(self):
        if self.username == 'sentry':
            raise Exception('You cannot delete the "sentry" user as it is required by Sentry.')
        return super(User, self).delete()

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        return super(User, self).save(*args, **kwargs)

    def has_perm(self, perm_name):
        warnings.warn('User.has_perm is deprecated', DeprecationWarning)
        return self.is_superuser

    def has_module_perms(self, app_label):
        warnings.warn('User.has_module_perms is deprecated', DeprecationWarning)
        return self.is_superuser

    def get_display_name(self):
        return self.name or self.email or self.username

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.username

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
