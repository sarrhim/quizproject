from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from authentification import views as authe_views



urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', authe_views.signup, name='signup'),

    ]