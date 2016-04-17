from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.contrib import admin
from wangblog.web.frontend.accounts import AccountsRegisterView, RegisterView
from wangblog.web.frontend.home import HomeView
from wangblog.api import urls

admin.autodiscover()


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'WangBlog.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^api/1/', include('wangblog.api.urls')),
                       url(r'^admin/', include(admin.site.urls)),

                       # url(r'^auth/login/', AuthLoginView.as_view(), name='auth-login')
                       url(r'^auth/login/', view='django.contrib.auth.views.login', kwargs={'template_name': 'loginsight/login.html'}),
                       url(r'^register', RegisterView.as_view(), name='register'),
                       url(r'^$', HomeView.as_view(), name='home'),
                       url(r'^accounts/login$', 'django.contrib.auth.views.login'),
                       url(
                           regex=r'^login',
                           view='django.contrib.auth.views.login',
                           kwargs={'template_name': 'loginsight/login.html'}
                       ),
                       url(r'^accounts/logout', 'django.contrib.auth.views.logout', {'next_page': reverse_lazy('home')}),
                       url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
                       )

