from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.gis.shortcuts import render_to_kml
from models import *
from vectorformats.Formats import Django, GeoJSON
from django.core import serializers
from django.contrib.gis.geos import Point, GEOSGeometry
from django.views.decorators.csrf import csrf_protect
import json
from django.http import QueryDict
from django.contrib.gis.measure import Distance, Area
import pyproj

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
	pnti = Point(-65.7833, -28.4667, srid=4326)
	pnti.transform(900913)
	loni,lati=pnti.coords
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
	pnti = Point(-65.7833, -28.4667, srid=4326)
	pnti.transform(900913)
	loni,lati=pnti.coords
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
	pnti = Point(-65.7833, -28.4667, srid=4326)
	pnti.transform(900913)
	loni,lati=pnti.coords
	#data = serializers.serialize('json',puntos)
	#return HttpResponse(data, mimetype='application/json')
	return render_to_response('world/poligonos.html', locals(), context_instance=RequestContext(request))


def distancia(request):
	if request.is_ajax():
		#dic= json.loads(request.body)
		q = QueryDict(request.body)
		dic= q.dict()
		x0= float(dic['puntos[0][x]'])
		y0= float(dic['puntos[0][y]'])
		x1= float(dic['puntos[1][x]'])
		y1= float(dic['puntos[1][y]'])
		pnt1= Point(x0,y0,srid=900913)
		pnt1.transform(4326)
		pnt2= Point(x1,y1,srid=900913)
		pnt2.transform(4326)
		print pnt1
		print pnt2
		calculo= pnt1.distance(pnt2)
		print calculo*100
		lon1,lat1=pnt1.coords
		lon2,lat2=pnt2.coords
		geod = pyproj.Geod(ellps="WGS84")
		angle1,angle2,distance = geod.inv(lon1, lat1, lon2, lat2)
		print "Distance is %0.2f meters" % distance
	return HttpResponse(calculo, mimetype='application/json')

def area(request):
	if request.is_ajax():
		#print request.body
		#q = json.loads(request.body)
		poligono= GEOSGeometry(request.body,srid=900913)
		poligono.transform(4326)
		print poligono.coords
		area= poligono.area
		print area
	return HttpResponse(area,mimetype='application/json')
# Create your views here.