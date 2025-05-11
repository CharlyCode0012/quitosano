from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
import uuid
from datetime import date, time
from ..supabase_client import supabase
from ..models.recepcion import Recepcion

def parse_recepcion(data: dict) -> Recepcion:
    return Recepcion(
        id_recepcion = uuid.UUID(data.get('id_recepcion')) if data.get('id_recepcion') else uuid.uuid4(),
        id_envio = uuid.UUID(data.get('id_envio')) if data.get('id_envio') else uuid.uuid4(),
        fecha_llegada = date(data["fecha_llegada"]),
        hora_llegada = time(data["hora_llegada"]),
        temperatura_llegada = float(data["temperatura_llegada"]),
        unidad_temperatura = data["unidad_temperatura"],
        nombre_producto = data["nombre_producto"],
        cantidad = float(data["cantidad"]),
        unidad = data["unidad"],
        observaciones = data["observaciones"],
        condiciones = data["condiciones"],
        recibido_por = data["recibido_por"]

    )

@require_http_methods(["GET"])
def lista_recepciones(request):
   response  =  supabase.table("envios").select("*").execute()
   return JsonResponse(response.data, safe = False)

    

@csrf_exempt
@require_http_methods(["POST"])
def crear_recepcion(request):
    try:
        data = json.loads(request.body)
        recepcion = parse_recepcion(data)
        recepcion_dict = recepcion.__dict__.copy()
        recepcion_dict["id_envio"]  =  str(recepcion.id_envio)
        recepcion_dict["id_recepcion"]  =  str(recepcion.id_recepcion)
        recepcion_dict["fecha_llegada"]  =  recepcion.fecha_llegada.isoformat()
        recepcion_dict["hora_llegada"]  =  recepcion.hora_llegada.isoformat()

        result = supabase.table("recepciones").insert(recepcion_dict).execute()
        return JsonResponse(result.data, safe = False)
    except Exception as e:
        return JsonResponse({"error": e}, status = 400)
    

@csrf_exempt
@require_http_methods(["PUT"])
def actualizar_recepcion(request, recepcion_id):
    try:
        data = json.loads(request.body)
        recepcion = parse_recepcion(data)
        recepcion_dict = recepcion.__dict__.copy()
        recepcion_dict["id_envio"]  =  str(recepcion.id_envio)
        recepcion_dict["id_recepcion"]  =  str(recepcion.id_recepcion)
        recepcion_dict["fecha_llegada"]  =  recepcion.fecha_llegada.isoformat()
        recepcion_dict["hora_llegada"]  =  recepcion.hora_llegada.isoformat()

        result = supabase.table("recepciones").update(recepcion_dict).eq("id_recepcion", str(recepcion_id)).execute()
        return JsonResponse(result.data, safe = False)
    except Exception as e:
        return JsonResponse({"error": e}, status = 400)

@csrf_exempt
@require_http_methods(["PUT"])
def eliminar_recepcion(request, recepcion_id):
    try:
       

        result = supabase.table("recepciones").delete().eq("id_recepcion", str(recepcion_id)).execute()
        return JsonResponse(result.data, safe = False)
    except Exception as e:
        return JsonResponse({"error": e}, status = 400)