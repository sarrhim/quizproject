from django.conf.urls import url
from django.contrib.auth import views as auth_views

from authentification import views as authe_views
from . import views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^signup/$', authe_views.signup, name='signup'),

    ]