
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Evento
from .models import Boleto
import json
from datetime import datetime,date
import random

# Create your views here.
def genkey(): 
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    charLength = len(chars)
    result=''
    for x in range(1,11):
        result += chars[random.randrange(0, charLength)]
    return result
     

class EventoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs) :
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):
        if(id>0):
            eventos=list(Evento.objects.filter(id=id).values())
            if len(eventos)>0:
                evento=eventos[0]
                datos={'message':"Success",'evento':evento}
            else:
                datos={'message':"Evento no encontrado"}
            return JsonResponse(datos)
        else:
            eventos=list(Evento.objects.values())
            if len(eventos)>0:
                datos={'message':"Success",'eventos':eventos}
            else:
                datos={'message':"Eventos no encontrado"}
            return JsonResponse(datos)
        
    def get_eventos(request):
        Nombre = request.GET['Nombre']
        
        eventos=list(Evento.objects.filter(Nombre__icontains=Nombre).values())
        print(eventos)
        if len(eventos)>0:
            
            datos={'message':"Success",'eventos':eventos}
        else:
                datos={'message':"Evento no encontrado"}
        return JsonResponse(datos)
        

    def post(self,request):
        jd=json.loads(request.body)
        Evento.objects.create(
            key_evento=jd['key_evento'],
            Nombre=jd['Nombre'],
            fecha_inicio=jd['fecha_inicio'],
            hora_inicio=jd['hora_inicio'],
            fecha_fin=jd['fecha_fin'],
            hora_fin=jd['hora_fin'],
            max_boletos=jd['max_boletos']
            )
        datos={'message':"Success"}
        return JsonResponse(datos)

    def put(self,request,id):
        jd=json.loads(request.body)
        print(jd)
        eventos=list(Evento.objects.filter(id=id).values())
        if len(eventos)>0:
            evento=Evento.objects.get(id=id)
            evento.key_evento=jd['key_evento']
            evento.Nombre=jd['Nombre']
            evento.fecha_inicio=jd['fecha_inicio']
            evento.hora_inicio=jd['hora_inicio']
            evento.fecha_fin=jd['fecha_fin']
            evento.hora_fin=jd['hora_fin']
            evento.max_boletos=jd['max_boletos']
            evento.save()
            datos={'messages':"Success"}  
        else:
            datos={'message':"Eventos no encontrado"}
        return JsonResponse(datos)
    
    def delete(self,request,id):
        eventos=list(Evento.objects.filter(id=id).values())
        if len(eventos)>0:
            Evento.objects.filter(id=id).delete()
            datos={'messages':"Success"}  
        else:
            datos={'message':"Eventos no encontrado"}
        return JsonResponse(datos)


class BoletoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs) :
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):
        if(id>0):
            boletos=list(Boleto.objects.filter(id=id).values())
            if len(boletos)>0:
                boleto=boletos[0]
                datos={'message':"Success",'boleto':boleto}
            else:
                datos={'message':"Boleto no encontrado"}
            return JsonResponse(datos)
        else:
            boletos=list(Boleto.objects.values())
            if len(boletos)>0:
                datos={'message':"Success",'boletos':boletos}
            else:
                datos={'message':"Boletos no encontrado"}
            return JsonResponse(datos)
        
    def get_boletos(request,id):
        if(id>0):
            boletos=list(Boleto.objects.filter( id_evento_id=id).values())
            
            if len(boletos)>0:
                
                datos={'message':"Successa",'boletos':boletos}
            else:
                datos={'message':"Boleto no encontrado"}
            return JsonResponse(datos)
        else:
            boletos=list(Boleto.objects.values())
            if len(boletos)>0:
                datos={'message':"Success",'boletos':boletos}
            else:
                datos={'message':"Boletos no encontrado"}
            return JsonResponse(datos)

    def post(self,request):
        jd=json.loads(request.body)
        
        evento_instancia =Evento.objects.get(id=jd['id_evento_id'])
        
        for x in range(1,(jd['boletos']+1)):
            key=genkey()
            Boleto.objects.create(
            id_evento=evento_instancia,
            key_boleto =key,
            comprador=jd['comprador'],
            status_canjeo=jd['status_canjeo'],
            status_active=jd['status_active']
            )

        datos={'message':"Success"}
        return JsonResponse(datos)

    
        