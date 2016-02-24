from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tienda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('tienda.apps.inicio.urls')),
    url(r'^ventas/', include('tienda.apps.ventas.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
