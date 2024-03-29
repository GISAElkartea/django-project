from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
        url(r'^grappelli/', include('grappelli.urls')),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^feedback/', include('feedback.urls')),
        url(r'^badbrowser/', include('django_badbrowser.urls')),
        #url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
