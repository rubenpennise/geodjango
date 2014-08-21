from django.contrib.gis import admin
from models import WorldBorder, PuntosInteres, Lineas,Poligonos
from django.contrib.gis.geos import Point

admin.site.register(WorldBorder, admin.GeoModelAdmin)

class PuntosInteresAdmin(admin.OSMGeoAdmin):
	list_display = ('name','descripcion')
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

class LineasAdmin(admin.OSMGeoAdmin):
	list_display = ('name','descripcion')
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

class PoligonosAdmin(admin.OSMGeoAdmin):
	list_display = ('name','descripcion')
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
admin.site.register(Lineas,LineasAdmin)
admin.site.register(Poligonos,PoligonosAdmin)

# Register your models here.
