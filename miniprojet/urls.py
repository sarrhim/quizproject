
from django.conf.urls import include,url
from django.contrib import admin
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('authentification.urls')),
    url(r'^quiz/', include('quiz.urls')),


]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


