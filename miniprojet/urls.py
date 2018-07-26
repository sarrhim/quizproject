
from django.conf.urls import include,url
from django.contrib import admin


urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('authentification.urls')),
    url(r'^quiz/', include('quiz.urls')),


]
