from django.conf.urls import patterns, include, url

from django.contrib.gis import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'geodjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('world.urls')),
    url(r'^calculos/$', 'world.views.calculos'),
    url(r'^kml/', 'world.views.allkml'),
)
