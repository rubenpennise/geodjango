from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.gis.shortcuts import render_to_kml
from models import *
from vectorformats.Formats import Django, GeoJSON
from django.core import serializers
from django.contrib.gis.geos import Point

def calculos(request):
	puntos = PuntosInteres.objects.all().count()
	return render_to_response('world/calculos.html',{'puntos':puntos})

def allkml(request):
	interes = PuntosInteres.objects.kml()
	return render_to_kml('gis/kml/placemarks.kml',{'places': interes})

def puntosjson(request):
	puntos = PuntosInteres.objects.all()
	djf = Django.Django(geodjango="geometry", properties=['name', 'descripcion'])
	geoj = GeoJSON.GeoJSON()
	string = geoj.encode(djf.decode(puntos))
	print string
	return render_to_response('world/leatflet.html', [string], context_instance=RequestContext(request))

def puntjson(request):
	puntos = PuntosInteres.objects.all()
	djf = Django.Django(geodjango="geometry", properties=['name', 'descripcion'])
	geoj = GeoJSON.GeoJSON()
	string = geoj.encode(djf.decode(puntos))
	data = serializers.serialize('json',puntos)
	print string
	return HttpResponse(string, mimetype='application/json') 

def jsonser(request):
	puntos = PuntosInteres.objects.all()
	djf = Django.Django(geodjango="geometry", properties=['name', 'descripcion'])
	geoj = GeoJSON.GeoJSON()
	data = geoj.encode(djf.decode(puntos))
	pnt = Point(-65.7833, -28.4667, srid=4326)
	pnt.transform(4269)
	lon,lat=pnt.coords
	#data = serializers.serialize('json',puntos)
	#return HttpResponse(data, mimetype='application/json')
	return render_to_response('world/gmap.html', locals(), context_instance=RequestContext(request))

def lineas(request):
	puntos = Lineas.objects.all()
	djf = Django.Django(geodjango="geometry", properties=['name', 'descripcion'])
	geoj = GeoJSON.GeoJSON()
	data = geoj.encode(djf.decode(puntos))
	pnt = Point(-65.7833, -28.4667, srid=4326)
	pnt.transform(4269)
	lon,lat=pnt.coords
	#data = serializers.serialize('json',puntos)
	#return HttpResponse(data, mimetype='application/json')
	return render_to_response('world/lineas.html', locals(), context_instance=RequestContext(request))

def poligonos(request):
	puntos = Poligonos.objects.all()
	djf = Django.Django(geodjango="geometry", properties=['name', 'descripcion'])
	geoj = GeoJSON.GeoJSON()
	data = geoj.encode(djf.decode(puntos))
	pnt = Point(-65.7833, -28.4667, srid=4326)
	pnt.transform(4269)
	lon,lat=pnt.coords
	#data = serializers.serialize('json',puntos)
	#return HttpResponse(data, mimetype='application/json')
	return render_to_response('world/poligonos.html', locals(), context_instance=RequestContext(request))
# Create your views here.