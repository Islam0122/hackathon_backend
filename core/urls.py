from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .drf_yasg import urlpatterns as urls_swagger

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/v1/patient/', include('apps.Patient.urls')),
                  path('api/v1/entry/', include('apps.Entry.urls')),
                  path('api/v1/', include('docs.urls')),
                  path('doctor/', include('personal_account.urls')),
              ] + urls_swagger
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
