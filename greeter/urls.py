from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

import hello

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(hello.urls)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
