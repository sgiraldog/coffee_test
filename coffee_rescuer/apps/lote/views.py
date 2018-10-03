from django.shortcuts import render
from apps.lote.models import Lote, DetalleLote
from apps.lote.form import HistorialForm
from django.contrib import messages
import json

#import os
# Create your views here.



def vista_lote(request,id_lote):
	lote = Lote.objects.get(id = id_lote)
	detalle_lote = lote.obtener_detalle_lote_actual()

	if detalle_lote:
		info_sensores = detalle_lote.obtener_info_sensores()
		context = {"info_sensores":info_sensores, "lote":lote, "etapa_hongo": detalle_lote.etapa_hongo}
	else:
		messages.info(request, "No hay información sobre este lote")
		context = {"lote":lote}
	return render(request,"lote/vistaLote.html",context)

def historial_lote(request, id_lote):
	historial = []

	lote = Lote.objects.get(id = id_lote)
	if request.method == "POST":
		form = HistorialForm(request.POST)
		if form.is_valid():
			start = form.cleaned_data['start']
			end = form.cleaned_data['end']
			if start > end:
				messages.info(request, "La fecha inicial debe ser menor o igual a la fecha final")
			else:
				historial = lote.obtener_detalle_rango(start, end)
				context = {"lote":lote, "historial": historial,"form":form}
				return render(request, 'lote/historialDatos.html',context)

	else:
		form = HistorialForm()
	
	detalle_lotes = DetalleLote.objects.filter(lote=lote).order_by('id')

	for detalle in detalle_lotes:
		detalle_sensores = detalle.obtener_info_sensores()
		etapa = detalle.etapa_hongo
		detalle_sensores['timestamp'] = detalle.obtener_fecha_formato_python()
		detalle_sensores['etapa'] = etapa
		historial.append(detalle_sensores)

	context = {"lote":lote, "historial": historial,"form":form}
	return render(request, 'lote/historialDatos.html',context)
