from django.contrib.gis import admin
from models import WorldBorder, PuntosInteres
from django.contrib.gis.geos import Point

admin.site.register(WorldBorder, admin.GeoModelAdmin)

class PuntosInteresAdmin(admin.OSMGeoAdmin):
	lis_display = ('name','name')
	fieldsets= (
		('Location Attributes',{'fields':(('name','descripcion'))}),
		('Editable Map View',{'fields':('geometry',)}),
		)
	def transformar():
		pnt = Point(-65.7833, -28.4667, srid=4326)
		pnt.transform(900913)
		return pnt.coords
	default_lon, default_lat = transformar()
	default_zoom = 8





admin.site.register(PuntosInteres,PuntosInteresAdmin)

# Register your models here.
