from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index , name='index'),
    url(r'^create/$', views.create_view, name='create_view'),
    url(r'^(?P<exam_id>[0-9]+)/$', views.detail,name='detail'),
    url(r'^createQuest/$', views.createExam, name='createExam'),
    url(r'^(?P<Quest_id>[0-9]+)/modifOne/$', views.modifOne, name='modifOne'),
    url(r'^(?P<question_id>[0-9]+)/deleteQuest/$', views.deleteQuest, name='deleteQuest'),
    url(r'^(?P<question_id>[0-9]+)/modifmulti/$',views.modifmulti, name='modifmulti'),
    url(r'^(?P<question_id>[0-9]+)/modifFree/$',views.modifFree, name='modifFree'),
  ]
"""
    url(r'^(?P<exam_id>[0-9]+)/reponse/$', views.reponse, name='reponse'),
    url(r'^(?P<exam_id>[0-9]+)/edit/$', views.edit, name='edit'),
   

    
    url(r'^secondeQuest/$', views.secondeQuest, name='secondeQuest'),
    url(r'^(?P<exam_id>[0-9]+)/addQuest/$', views.addQuest, name='addQuest'),
    url(r'^(?P<exam_id>[0-9]+)/deleteEXam/$', views.deleteEXam, name='deleteEXam'),
    
    url(r'^(?P<exam_id>[0-9]+)/passe/$', views.passe, name='passe'),
    url(r'^(?P<exam_id>[0-9]+)/passe/(?P<Quest_id>[0-9]+)$', views.passeQuest, name='passeQuest'),
    """


