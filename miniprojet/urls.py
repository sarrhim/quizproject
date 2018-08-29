from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.views.generic.base import RedirectView

from . import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('authentification.urls')),
    url(r'^quiz/', include('quiz.urls')),
    path('', RedirectView.as_view(url='/auth/', permanent=True)),



]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


