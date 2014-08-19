from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.gis.shortcuts import render_to_kml
from models import *

def calculos(request):
	puntos = PuntosInteres.objects.all().count()
	return render_to_response('world/calculos.html',{'puntos':puntos})

def allkml(request):
	interes = PuntosInteres.objects.all()
	return render_to_kml('gis/kml/placemarks.kml',{'places': interes})

# Create your views here.