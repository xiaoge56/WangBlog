
# -*- coding: utf-8 -*-
"""
author : wanghe
company: LogInsight
email_ : wangh@loginsight.cn
file: accounts.py
time   : 16/4/16 下午5:21  
"""
from __future__ import absolute_import
import pytz

from captcha.fields import ReCaptchaField
from datetime import datetime
from django import forms
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _
from wangblog.models.user import User


# at runtime we decide whether we should support recaptcha
# TODO(dcramer): there **must** be a better way to do this
if settings.RECAPTCHA_PUBLIC_KEY:
    class CaptchaForm(forms.Form):
        def __init__(self, *args, **kwargs):
            captcha = kwargs.pop('captcha', True)
            super(CaptchaForm, self).__init__(*args, **kwargs)
            if captcha:
                self.fields['captcha'] = ReCaptchaField()

    class CaptchaModelForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            captcha = kwargs.pop('captcha', True)
            super(CaptchaModelForm, self).__init__(*args, **kwargs)
            if captcha:
                self.fields['captcha'] = ReCaptchaField()

else:
    class CaptchaForm(forms.Form):
        def __init__(self, *args, **kwargs):
            kwargs.pop('captcha', None)
            super(CaptchaForm, self).__init__(*args, **kwargs)

    class CaptchaModelForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            kwargs.pop('captcha', None)
            super(CaptchaModelForm, self).__init__(*args, **kwargs)


def _get_timezone_choices():
    results = []
    for tz in pytz.common_timezones:
        now = datetime.now(pytz.timezone(tz))
        offset = now.strftime('%z')
        results.append((int(offset), tz, '(GMT%s) %s' % (offset, tz)))
    results.sort()

    for i in range(len(results)):
        results[i] = results[i][1:]
    return results

TIMEZONE_CHOICES = _get_timezone_choices()


class AuthenticationForm(CaptchaForm):
    username = forms.CharField(
        label=_('Account'), max_length=128, widget=forms.TextInput(
            attrs={'placeholder': _('username or email'),
        }),
    )
    password = forms.CharField(
        label=_('Password'), widget=forms.PasswordInput(
            attrs={'placeholder': _('password'),
        }),
    )

    error_messages = {
        'invalid_login': _("Please enter a correct %(username)s and password. "
                           "Note that both fields may be case-sensitive."),
        'no_cookies': _("Your Web browser doesn't appear to have cookies "
                        "enabled. Cookies are required for logging in."),
        'inactive': _("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        If request is passed in, the form will validate that cookies are
        enabled. Note that the request (a HttpRequest object) must have set a
        cookie with the key TEST_COOKIE_NAME and value TEST_COOKIE_VALUE before
        running this validation.
        """
        self.request = request
        self.user_cache = None
        super(AuthenticationForm, self).__init__(*args, **kwargs)

        # Set the label for the "username" field.
        UserModel = get_user_model()
        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        if not self.fields['username'].label:
            self.fields['username'].label = capfirst(self.username_field.verbose_name)

    def clean_username(self):
        value = (self.cleaned_data.get('username') or '').strip()
        if not value:
            return
        return value.lower()

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username,
                                           password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'] % {
                        'username': self.username_field.verbose_name
                    })
            elif not self.user_cache.is_active:
                raise forms.ValidationError(self.error_messages['inactive'])
        self.check_for_test_cookie()
        return self.cleaned_data

    def check_for_test_cookie(self):
        if self.request and not self.request.session.test_cookie_worked():
            raise forms.ValidationError(self.error_messages['no_cookies'])

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache


class RegistrationForm(CaptchaModelForm):
    username = forms.EmailField(
        label=_('Email'), max_length=128,
        widget=forms.TextInput(attrs={'placeholder': 'you@example.com'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'something super secret'}))

    class Meta:
        fields = ('username',)
        model = User

    def clean_username(self):
        value = (self.cleaned_data.get('username') or '').strip()
        if not value:
            return
        if User.objects.filter(username__iexact=value).exists():
            raise forms.ValidationError(_('An account is already registered with that email address.'))
        return value.lower()

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = user.username
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class ChangePasswordRecoverForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())

