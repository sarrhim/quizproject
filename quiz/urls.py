from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index , name='index'),
    url(r'^create/$', views.create_view, name='create_view'),
    url(r'^(?P<exam_id>[0-9]+)/$', views.detail,name='detail'),
  ]
