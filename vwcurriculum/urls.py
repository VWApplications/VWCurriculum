from django.conf.urls import url, include, handler404, handler500
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from vwcurriculum.core import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('vwcurriculum.core.urls')),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = views.error_404
handler500 = views.error_500
