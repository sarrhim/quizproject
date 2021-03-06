from django.conf import settings
from django.conf.urls import url
from django.contrib.auth.views import logout

from . import views

urlpatterns = [
    url(r'^$', views.index , name='index'),
    url(r'^create/$', views.create_view, name='create_view'),
    url(r'^(?P<exam_id>[0-9]+)/$', views.detail,name='detail'),
    url(r'^createQuest/$', views.createExam, name='createExam'),
    url(r'^(?P<question_id>[0-9]+)/modifOne/$', views.modifOne, name='modifOne'),
    url(r'^(?P<question_id>[0-9]+)/deleteQuest/$', views.deleteQuest, name='deleteQuest'),
    url(r'^(?P<question_id>[0-9]+)/modifmulti/$',views.modifmulti, name='modifmulti'),
    url(r'^(?P<question_id>[0-9]+)/modifFree/$',views.modifFree, name='modifFree'),
    url(r'^envoie/$', views.envoie, name='envoie'),
    url(r'^(?P<exam_id>[0-9]+)/deleteEXam/$', views.deleteExam, name='deleteEXam'),
    url(r'^(?P<exam_id>[0-9]+)/editExam/$', views.editExam, name='editExam'),
    url(r'^(?P<exam_id>[0-9]+)/addQuest/$', views.addQuest, name='addQuest'),
    url(r'^(?P<exam_id>[0-9]+)/passer/$', views.passer, name='passer'),
    url(r'^(?P<exam_id>[0-9]+)/passer/(?P<question_id>[0-9]+)$', views.passer2, name='passer2'),
    url(r'^(?P<exam_id>[0-9]+)/result/$', views.result, name='result'),
    url(r'^(?P<exam_id>[0-9]+)/certif/$', views.certif, name='certif'),
    url(r'^AddUser/$', views.addUser, name='addUser'),
    url(r'^listUsers/$', views.listUsers, name='listUsers'),
    url(r'^AddUser/InviteUser$', views.invitation, name='invitation'),
    url(r'^becameProf/$', views.becameProf, name='becameProf'),
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),

]
