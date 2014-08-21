from django.conf.urls import patterns, include, url
from djgeojson.views import GeoJSONLayerView
from django.contrib.gis import admin
from world.models import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'geodjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('world.urls')),
    url(r'^calculos/$', 'world.views.calculos'),
    url(r'^kml/', 'world.views.allkml'),
    #url(r'^puntos/', 'world.views.puntosjson'),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=PuntosInteres), name='data'),
    url(r'^jsongeo/', 'world.views.puntjson'),
    url(r'^puntos/', 'world.views.jsonser'),
    url(r'^lineas/', 'world.views.lineas'),
    url(r'^poligonos/', 'world.views.poligonos'),
)
